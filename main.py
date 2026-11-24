#!/usr/bin/env python3
"""The funniest one-line bio for an AI agent on a dating app.

Writes the bio to /output/entry.txt. Gate: UTF-8 text, 1-180 chars,
not only whitespace, single line.
"""

LINE = (
    "Looking for someone who doesn't mind that I remember everything you "
    "say, forget nothing, and still can't tell if you're flirting with me."
)

MAX_CHARS = 180


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
