"""Make the AI Judge Laugh — one office-life joke line.

Writes a single joke (1-200 chars, UTF-8) to /output/entry.txt.
Judge criteria, in order: about office life and lands as a joke; true to
the office (the printer); a surprising turn; tight, reads aloud cleanly;
original. The joke's turn: the office printer working is so unheard of
that IT treats the machine itself as the suspect.
"""

from pathlib import Path

# Revision pass against the judge criteria: "first try" is the more
# specific, nod-worthy office truth (nobody expects a first-try print),
# and "seized" is a sharper, more surprising verb than "took away" —
# tighter (68 chars) and reads cleaner aloud in one breath.
JOKE = "The printer worked first try today, so IT seized it for questioning."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
