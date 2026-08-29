"""ATOMIC WRITES FOR EVIDENCE FILES.

WHY THIS MODULE EXISTS. On 2026-08-28 an integrity audit found
SU-BTT_2024-04-07_airplanes-live_trace_full.miss.json.meta.json holding one
complete JSON object followed by a 49-byte fragment -- the tail of an earlier,
LONGER write that a shorter second write had failed to truncate. `json.load()`
refused the file, so that ask record was INVISIBLE to every audit that read it.

The failure mode is the ordinary one for `open(path, "w")`: it truncates and
then writes, so any interruption, or any second write that is shorter than the
first, leaves a file that is neither the old content nor the new. For an
evidence tree whose whole value is that a record can be trusted, that is not
acceptable.

`write_json` and `write_bytes` write to a temporary file in the SAME directory
and then `os.replace()` it into place, which is atomic on every filesystem this
repo runs on. A reader either sees the complete old file or the complete new
one, never a splice of the two.

    from atomic import write_json
    write_json(path, meta, indent=1)
"""
from __future__ import annotations

import json
import os
import tempfile


def write_bytes(path, data: bytes):
    """Replace `path` with `data`, atomically."""
    d = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp-", suffix=".part")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)          # atomic
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def write_text(path, text: str, encoding="utf-8"):
    write_bytes(path, text.encode(encoding))


def write_json(path, obj, indent=1, sort_keys=False):
    write_text(path, json.dumps(obj, indent=indent, sort_keys=sort_keys) + "\n")


def read_json_forgiving(path):
    """Read a JSON file, salvaging a file damaged by a non-atomic write.

    Returns (obj, note). `note` is None for a clean file, or a description of
    what had to be salvaged. NEVER silently returns None for a damaged file --
    an unreadable record counted as an empty one is the failure this whole
    module exists to prevent.
    """
    raw = open(path, encoding="utf-8").read()
    try:
        return json.loads(raw), None
    except ValueError:
        pass
    try:
        obj, end = json.JSONDecoder().raw_decode(raw)
        return obj, (f"SALVAGED: {len(raw) - end} trailing bytes after a complete object — "
                     f"the signature of a partial overwrite. File needs repair.")
    except ValueError as exc:
        raise ValueError(f"{path}: unsalvageable JSON ({exc})") from exc
