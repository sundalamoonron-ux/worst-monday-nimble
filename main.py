#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes exactly one funny line (<=140 chars) about an AI agent's worst
Monday to /output/entry.txt.

Line chosen by a pairwise tournament over 10 original candidates
(judge criteria: on-theme, surprise/twist, concrete detail, clear
voice, fresh): winner 4-0, runner-up was the 6am-page/printer line.
"""

import os

LINE = (
    "My worst Monday: I hallucinated a fix, deployed it with total "
    "confidence, and by lunch the error logs filed a complaint about me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
