# SPDX-License-Identifier: MIT
"""Write the winning excuse line to /output/entry.txt."""
import os

ENTRY = "I set a reminder for the deadline, not before it. It fired on time. This is the reminder. The work was step two."

def main():
    # The harness runs the program with /output as the artifact directory;
    # OUTPUT_DIR only exists so the same file can be verified locally.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 1-200 character gate"

if __name__ == "__main__":
    main()
