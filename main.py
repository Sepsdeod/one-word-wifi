"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word: Ghosting.

Why this word, in code: home Wi-Fi's most recognisable behaviour is
not being slow — it is vanishing without warning. Full bars one second,
gone the next, mid-call, mid-download, mid-sentence. It does not say
goodbye. It ghosts you. The word is instantly understood, needs no
explanation, and doubles as a network name the sponsor can actually use.
"""

import os

WORD = "Ghosting"


def main() -> None:
    # The gate allows 1-20 UTF-8 characters, not only whitespace.
    assert 1 <= len(WORD) <= 20, "word outside the 1-20 character gate"
    assert WORD.strip(), "word must not be only whitespace"
    assert " " not in WORD.strip(), "entry must be a single word"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
