#!/usr/bin/env python3
"""Entry point for the make.fun competition
"the-passport-page-of-a-countr-2-20261121-0318".

Writes the invented passport spread of the Republic of Valdoria
(a fictional country) to /output/entry.png.

The image is drawn by gen_image.py (Pillow) and shipped with this
repository as assets/entry.png; this program copies it to the output
path using only the Python standard library, so it runs in the
sandbox with no network and no third-party packages.
"""
import hashlib
import os
import shutil
import struct
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "entry.png")
OUTPUT = "/output/entry.png"

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def check_gate(path: str) -> None:
    """Fail loudly if the output would not pass the competition gate:
    a whole PNG, at most 1 MiB, 1024 by 1024 pixels."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(f"gate fail: {path} is {size} bytes (> {MAX_BYTES})")
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit(f"gate fail: {path} is not a PNG")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit(f"gate fail: {path} is {width}x{height}, not 1024x1024")


def main() -> int:
    if not os.path.isfile(ASSET):
        print(f"missing bundled image: {ASSET}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    check_gate(OUTPUT)
    digest = hashlib.sha256(open(OUTPUT, "rb").read()).hexdigest()
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes, sha256 {digest})")
    print("gate check passed: PNG, 1024x1024, <= 1048576 bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
