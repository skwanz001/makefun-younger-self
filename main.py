"""One Line to Your Younger Self.

Writes the single line to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "Kid, stop saving the good shoes for a day that never comes: "
    "wear them to the warung and let the mud keep them."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk is exactly the line, nothing else.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt content mismatch"


if __name__ == "__main__":
    main()
