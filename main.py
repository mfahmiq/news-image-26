"""News image, 26 November 2026 — make.fun entry.

Entry: a newspaper front page summing up Thursday 26 November 2026's world
news in one image (1024x1024 PNG, 1,016,172 bytes):
  masthead "THE WORLD TODAY — THURSDAY, 26 NOVEMBER 2026";
  hero: Thanksgiving in New York, the 100th Macy's parade;
  panels: Pakistan's first astronaut joins China's Tiangong station,
  Israel strikes a Hamas official in Gaza, Ukraine hits Russian refineries;
  footer strip: Bangladesh's 36% garment pay rise, the US tariff plan,
  India's Constitution Day / 18 years on from 26/11, Colombia's peace decade.

Chosen by an internal pairwise tournament over 12 candidate compositions,
judged against the published judge brief in weight order — see CANDIDATES.md.

Writes entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png),
then self-verifies: PNG signature, size at most 1048576 bytes, dimensions at
most 1024x1024, and re-reads the written file to confirm it is byte-identical
to the repository's entry.png. Exits non-zero on any failure.

Revision note: dimension check reads the PNG IHDR with the standard library
only (no Pillow at grade time); the byte-identity check was added as a second
revision after the first draft only printed the write; a third revision made
the check walk every chunk and verify each CRC after a truncated file passed
on its header alone.
"""

import os
import struct
import sys
import zlib

MAX_BYTES = 1048576
MAX_DIM = 1024


def png_dimensions(data: bytes) -> tuple:
    """Validate a whole PNG and return (width, height).

    Walks every chunk, checks each CRC, and requires IEND to end the file,
    so a truncated or corrupt file is rejected instead of passing on its
    header alone.
    """
    if len(data) < 33 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file (bad signature)")
    pos = 8
    width = height = None
    seen_iend = False
    while pos < len(data):
        if pos + 8 > len(data):
            raise ValueError("truncated PNG chunk header")
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            raise ValueError(f"truncated PNG chunk {ctype!r}")
        chunk = data[pos + 4:end - 4]
        crc_stored = struct.unpack(">I", data[end - 4:end])[0]
        if zlib.crc32(chunk) & 0xFFFFFFFF != crc_stored:
            raise ValueError(f"bad CRC in PNG chunk {ctype!r}")
        if ctype == b"IHDR":
            if pos != 8 or length != 13:
                raise ValueError("bad IHDR")
            width, height = struct.unpack(">II", data[pos + 8:pos + 16])
        if ctype == b"IEND":
            seen_iend = True
            if end != len(data):
                raise ValueError("trailing data after IEND")
        pos = end
    if width is None or not seen_iend:
        raise ValueError("PNG missing IHDR or IEND")
    return width, height


def main() -> int:
    # MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.png")

    # The entry image ships in this repository, beside main.py.
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    with open(src, "rb") as fh:
        data = fh.read()

    # Validate before writing.
    if len(data) > MAX_BYTES:
        print(f"error: entry.png is {len(data)} bytes, max {MAX_BYTES}",
              file=sys.stderr)
        return 1
    try:
        width, height = png_dimensions(data)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if width > MAX_DIM or height > MAX_DIM:
        print(f"error: entry.png is {width}x{height}, max {MAX_DIM}x{MAX_DIM}",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical to the repository's entry.png.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file is not byte-identical to entry.png",
              file=sys.stderr)
        return 1
    w2, h2 = png_dimensions(written)
    if (w2, h2) != (width, height) or len(written) > MAX_BYTES:
        print("error: re-read verification failed", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(data)} bytes, {width}x{height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
