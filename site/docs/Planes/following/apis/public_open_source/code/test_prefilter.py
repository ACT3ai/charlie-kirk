#!/usr/bin/env python3
"""Regression test for the geo_sweep byte pre-filter.

THE DEFECT THIS GUARDS AGAINST, so nobody reintroduces it:

    math.floor(-111.73) == -112,  but a trace file PRINTS "-111.73".

The pre-filter builds substring tokens like b",-111." out of the integer part of
a coordinate. Building them with math.floor() shifted every western-hemisphere
band one degree west, so the EASTERN edge of every US circle was never examined
-- an average of 28.7% of each event circle's area, and 50.9% of the Salt Lake
City circle, which is why the 2026-08 sweep missed SU-BTT on the ground at Provo
on 2024-04-23. That aircraft-day is held in full by the per-tail route, which is
how the defect was caught rather than shipped.

The property that must always hold, and that this test checks by brute force:

    For ANY point genuinely inside a circle, the tokens generated for that
    circle must contain both that point's printed latitude token and its
    printed longitude token.

A pre-filter is allowed to be over-inclusive. It is never allowed to reject a
point that is actually inside a circle.

    python3 test_prefilter.py
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geo_sweep import prefilter_patterns  # noqa: E402

RADIUS_MI = 50.0


def token(value):
    """The exact bytes a trace file's printed coordinate contributes."""
    return ("," + f"{value:.6f}".split(".")[0] + ".").encode()


def check(lat, lon, seed_points=12):
    lats, lons = prefilter_patterns([dict(lat=lat, lon=lon, radius_mi=RADIUS_MI)])
    rnd = random.Random(f"{lat},{lon}")
    for _ in range(seed_points):
        bearing = rnd.uniform(0, 2 * math.pi)
        dist_deg = rnd.uniform(0, RADIUS_MI * 0.98) / 69.0
        plat = lat + dist_deg * math.cos(bearing)
        plon = lon + dist_deg * math.sin(bearing) / max(0.15, math.cos(math.radians(lat)))
        if token(plat) not in lats or token(plon) not in lons:
            return (lat, lon, plat, plon, token(plat).decode(), token(plon).decode())
    return None


def main():
    # The two circles from the real defect, first and by name.
    named = [("Salt Lake City", 40.704200, -111.986400),
             ("Orem", 40.298100, -111.699400),
             ("Provo point in the SLC circle", 40.230700, -111.728800),
             ("Cairo", 30.100000, 31.400000),
             ("just west of Greenwich", 51.500000, -0.100000),
             ("just east of Greenwich", 51.500000, 0.100000),
             ("equator/meridian", 0.100000, -0.100000)]
    bad = 0
    for name, lat, lon in named:
        fail = check(lat, lon, seed_points=200)
        print(f"{'FAIL' if fail else 'ok  '}  {name:32} ({lat}, {lon})")
        if fail:
            bad += 1
            print(f"        point {fail[2]:.6f},{fail[3]:.6f} needs {fail[4]} {fail[5]}")

    # The specific miss, asserted directly rather than sampled.
    lats, lons = prefilter_patterns([dict(lat=40.7042, lon=-111.9864, radius_mi=50.0)])
    slc_catches_provo = b",-111." in lons and b",40." in lats
    print(f"{'ok  ' if slc_catches_provo else 'FAIL'}  SLC circle generates the token Provo's longitude needs")
    if not slc_catches_provo:
        bad += 1

    rnd = random.Random(20260828)
    for _ in range(6000):
        fail = check(rnd.uniform(-70, 70), rnd.uniform(-179.5, 179.5))
        if fail:
            bad += 1
            print(f"FAIL  random circle {fail[0]:.4f},{fail[1]:.4f} rejects an interior point "
                  f"{fail[2]:.4f},{fail[3]:.4f} (needs {fail[4]} {fail[5]})")
            break
    else:
        print("ok    6,000 random circles x 12 interior points each: none rejected")

    print("\nFAILED" if bad else "\nPASSED")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
