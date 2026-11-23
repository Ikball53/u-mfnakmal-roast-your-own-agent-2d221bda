"""Roast Your Own Agent entry: emit a single playful self-roast line."""

from pathlib import Path

# Short setup up front; the semicolon lands last as the punchline.
ROAST_LINE = (
    "My agent rewrites 2,000 working lines before breakfast, then asks "
    "permission, makes a backup, and apologizes to delete one semicolon."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ROAST_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
