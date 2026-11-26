#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message (make.fun).

Writes one commit message -- the note an AI agent leaves in the log
after a long night of chasing down and fixing its own bugs -- to
/output/entry.txt. Standard library only, no network, no randomness:
every run writes byte-identical output.
"""

import os
from pathlib import Path

TEXT = (
    # The joke is the loop of self-repair: the agent wrote the typo,
    # defended it in a comment, fixed it twice -- and the wrong comment
    # survives as a named artifact. One line, 119 characters.
    "4am: the bug was a typo I wrote, then defended in a comment, "
    "then fixed twice. The comment is still there. It is wrong."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
