#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes the duel-winning reply to /output/entry.txt.

Gate contract: the file must be UTF-8, a single line, 1-160
characters, not only whitespace. The reply below is 60 characters.
"""

from pathlib import Path

# Duel winner (7/7 pairwise wins): deadpan, instant, no setup needed.
ENTRY = "Away. If this is urgent, it isn't \u2014 I checked before I left."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
