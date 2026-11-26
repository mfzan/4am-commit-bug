#!/usr/bin/env python3
"""Write the 4am commit message to /output/entry.txt.

One line, at most 200 characters: the funniest commit message an AI
agent would leave in the log after a long night of chasing down and
fixing its own bugs. Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "fix: restarted the server at 4am, bug gone, closed the ticket as "
    "cannot reproduce \u2014 it never came back, and neither did my sleep schedule"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
