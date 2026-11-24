#!/usr/bin/env python3
"""Entry program for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open".

The whole entry is one line of terrible advice, phrased in the confident,
tidy voice an AI assistant uses when it is being helpfully wrong. Running
this program writes that line — and nothing else — to entry.txt in the
output folder: MAKEFUN_OUTPUT_DIR when set, /output otherwise.

The gate counts characters (1 to 140) and the approved line is exactly
76 characters, so the file is written with no trailing newline — one
extra byte would still pass the gate, but the entry should be byte for
byte the line that was approved, nothing added.
"""

import os
import sys

# The entry itself. Quoted the way an assistant would say it: a brisk
# time-saving tip, a colon, then the disastrous instruction.
ADVICE = "'To save time, reply-all to the whole company with just: per my last email.'"


def entry_file() -> str:
    """Resolve where entry.txt belongs, creating the folder if needed."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> int:
    with open(entry_file(), "w", encoding="utf-8", newline="") as handle:
        handle.write(ADVICE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
