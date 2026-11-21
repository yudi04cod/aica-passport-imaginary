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
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "entry.png")
OUTPUT = "/output/entry.png"

MAX_BYTES = 1_048_576


def main() -> int:
    if not os.path.isfile(ASSET):
        print(f"missing bundled image: {ASSET}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    digest = hashlib.sha256(open(OUTPUT, "rb").read()).hexdigest()
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
