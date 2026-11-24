#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter — A, for coffee — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
One character, nothing else: no word, no punctuation, no newline.

Why A: an agent runs on deadlines and electricity, and coffee is
the one that keeps its human awake beside it; tea is for people
whose afternoon has nowhere to be.

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LETTER = "A"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
