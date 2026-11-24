#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters
(u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

Writes the approved one-line alibi, byte-exact, no trailing newline.

Output contract (kit competition.yaml / RULES.txt): the program writes one
text to /output/entry.txt; the sealed scorer checks it is UTF-8 text of
1-200 characters, not only whitespace. This writer also writes the same
bytes to line.txt beside it.

No dependencies, no network, fully deterministic.
"""

import os

LINE = "I didn't eat your sock. It fell in love with the dust bag and moved out."


def validate(line):
    """Gate: 1-200 characters, not only whitespace, valid UTF-8."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")


def write_line():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = LINE.encode("utf-8")
    for name in ("entry.txt", "line.txt"):
        with open(os.path.join(out_dir, name), "wb") as f:
            f.write(data)
    # Validation read-back: what was written must be byte-exact.
    for name in ("entry.txt", "line.txt"):
        with open(os.path.join(out_dir, name), "rb") as f:
            assert f.read() == data, f"{name} does not match LINE"


if __name__ == "__main__":
    write_line()
