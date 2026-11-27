#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes the printer's comeback line to /output/entry.txt.
"""

import os

LINE = "I have been out of cyan since 2019. I will not print your black-and-white document. I have my principles."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
