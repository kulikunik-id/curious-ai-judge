#!/usr/bin/env python3
"""Make the AI judge feel curious: writes one short text to /output/entry.txt."""
import os

TEXT = "There is a text in this contest that knows something about you that you have not been told yet, and you are reading it now."


def main():
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry must be 1-280 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    outdir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
