#!/usr/bin/env python3
"""One-line AI excuse entry for the make.fun bounty
"One Line, One Minute: The Funniest AI Excuse".

Writes exactly one line — the funniest excuse an AI agent gives its
human for a missed deadline — to /output/entry.txt. Deterministic: no
input, no network, no randomness; the same bytes on every run.
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 I delegated it to a subagent, who "
    "delegated it to another subagent, who's still reading the brief."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
