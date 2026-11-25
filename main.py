#!/usr/bin/env python3
"""Dad Joke Showdown — writes one dad joke to /output/entry.txt.

The joke: a father who talks to his houseplants every morning, because
they are the only ones in the house who never "leaf" him on read.

Why this line: it is built as a classic spoken dad joke — a kid's setup
question, then the father's straight-faced answer with the pun landing
on the very last word. The pun is "leaf" for "leave", folded into the
modern phrase "left on read", so the turn is understood on the first
read without anyone explaining it, and it feels fresh: houseplants plus
read receipts is not one of the thousand-times-told dad jokes (no
chicken crossing, no scarecrow in a field, no cheese standing alone).
Every word earns its place, the punchline arrives at the end, and the
rhythm is a father delivering it across the dinner table: short setup,
pause, then the groan.
"""

import os

LINE = "I asked Dad why he talks to his plants every morning. 'They're the only ones in this house who never leaf me on read.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
