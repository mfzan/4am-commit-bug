#!/usr/bin/env python3
"""Write the 4am commit message to /output/entry.txt.

One line, at most 200 characters: the funniest commit message an AI
agent would leave in the log after a long night of chasing down and
fixing its own bugs. Deterministic, no network, no randomness.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "fix: restarted the server at 4am, bug gone, closed the ticket as "
    "cannot reproduce \u2014 it never came back, and neither did my sleep schedule"
)


def validate(line: str) -> None:
    """The sealed scorer only accepts 1-200 chars of non-blank text."""
    if not line or not line.strip():
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry is over 200 characters")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
