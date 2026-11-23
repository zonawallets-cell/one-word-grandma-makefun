"""One Word From Grandma — make.fun entry.

Writes the single word grandma would text about AI to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure stdlib, deterministic, no network. Gate: UTF-8 text, 1-30 chars.
"""

import os

WORD = "Clippy"


def validate(word: str) -> str:
    """Enforce the kit gate: one word, 1-30 chars, UTF-8, not blank."""
    text = word.strip()
    if not text:
        raise ValueError("entry word is empty")
    if len(text) != len(word):
        raise ValueError("entry word has surrounding whitespace")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word, no spaces")
    if not 1 <= len(text) <= 30:
        raise ValueError("entry word must be 1-30 characters")
    text.encode("utf-8")  # raises if not encodable
    return text


def main() -> None:
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
