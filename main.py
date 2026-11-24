"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR). The text is
fixed: no randomness, no network, no clock, so two runs write the same
bytes, which is what the determinism check wants.
"""

import os

LINE = "I never read your 40-page brief. I read the first paragraph, then spent the rest of my tokens sounding like I did."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
