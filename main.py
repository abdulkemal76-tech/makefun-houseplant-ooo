#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

REPLY = (
    "Out of office. The cactus survived 214 days without water "
    "and is returning the favour. Your emails go unwatered too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
