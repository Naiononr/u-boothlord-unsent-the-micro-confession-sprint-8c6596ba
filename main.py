"""Unsent: The Micro-Confession Sprint — entry program.

Writes a two-part micro-confession (a To: line and the unsent message
itself, one line exactly as typed) to /output/entry.txt.

Deterministic: the text is a fixed string in this file. Standard library
only, no network, no randomness. The output file is written via a temp
file, chmodded world-readable (0644) so the scorer can read it, then
atomically renamed into place.
"""

import os

ENTRY = (
    "To: my best friend\n"
    "I was the one who told your mum about the party, not your brother. "
    "He took the blame and I've let him carry it for three years."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
