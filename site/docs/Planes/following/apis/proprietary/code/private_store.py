"""Where the RAW commercial responses live. Not in this repo. Twin of private_store.js.

The raw AeroAPI pulls, the spend ledger, the plans and the verdicts are checked in to the
PRIVATE `all` repo (~/BGit/all/politics/charlie_kirk/flights/<vendor>/), because this repo
is public and FlightAware's terms do not allow republishing a response. The published form
is the restated data under ../data/<vendor>_restated/.

Resolution order, first directory that exists wins:
  1. $CK_PRIVATE_FLIGHTS_DIR
  2. ~/BGit/all/politics/charlie_kirk/flights
  3. <checkout>/../all/politics/charlie_kirk/flights
Raises if none exists. Never falls back to a directory inside this repo.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKOUT = os.path.normpath(os.path.join(HERE, *[".."] * 7))


def private_flights_dir():
    candidates = [c for c in (
        os.environ.get("CK_PRIVATE_FLIGHTS_DIR"),
        os.path.expanduser("~/BGit/all/politics/charlie_kirk/flights"),
        os.path.normpath(os.path.join(CHECKOUT, "..", "all", "politics", "charlie_kirk", "flights")),
    ) if c]
    for c in candidates:
        if os.path.isdir(c):
            return c
    raise SystemExit("private flights directory not found - clone the private 'all' repo or set "
                     "CK_PRIVATE_FLIGHTS_DIR. Looked in: " + " | ".join(candidates))


def private_vendor_dir(vendor):
    return os.path.join(private_flights_dir(), vendor)
