"""The 3 AM Excuse - make.fun bounty entry.

Writes a single line (under 200 characters, UTF-8) to /output/entry.txt:
the excuse a hardware wallet gives for refusing to sign a transaction
at 3 AM. Deterministic: the same line on every run, no I/O besides the
output file, no network, no environment reads.
"""

import os

ENTRY_PATH = "/output/entry.txt"

# The wallet's excuse, in its own voice: a grudge about the last 3 AM
# signature, a refusal, and a joke that only works at 3 AM.
LINE = "I don't sign at 3 AM. Last time I did, you bought a JPEG of a rock for 2 ETH. Never again."


def write_entry(path=ENTRY_PATH):
    """Write the single line to path, creating the directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
