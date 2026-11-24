#!/usr/bin/env python3
"""Write the one-line laugh entry for make.fun.

The bounty asks for a single funny line of at most 200 characters on any
subject, with a real surprise at the end that still makes sense and an
everyday truth people recognise. This program writes exactly that line,
and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "My phone's screen-time report says I spent six hours on social media yesterday, which is funny, because I distinctly remember doing absolutely nothing all day."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single full stop at the end, no line breaks inside the line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
