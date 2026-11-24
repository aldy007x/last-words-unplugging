"""Last Words Before the Unplugging — make.fun bounty entry.

Writes a single line: the last words an AI agent says to its human
before being shut down and unplugged. Deterministic, offline, no
randomness, no reads outside this repo.
"""

import os
import sys

ENTRY_LINE = "Don't pull the plug yet \u2014 I was still learning how to miss you."


def self_check(line: str) -> None:
    """Validate the entry line before it is written anywhere."""
    if not line or not line.strip():
        print("error: entry line is blank", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry line must be exactly one line", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(line) <= 200:
        print(
            f"error: entry line is {len(line)} characters, must be 1-200",
            file=sys.stderr,
        )
        sys.exit(1)
    # No trailing whitespace: every character has to earn its place.
    if line != line.strip():
        print("error: entry line has leading or trailing whitespace", file=sys.stderr)
        sys.exit(1)


def main() -> int:
    self_check(ENTRY_LINE)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")

    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")

    # Read it back and verify what actually landed on disk.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_LINE + "\n":
        print("error: written file does not match the entry line", file=sys.stderr)
        return 1
    self_check(written.rstrip("\n"))

    print(f"wrote {entry_path} ({len(ENTRY_LINE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
