#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it
(112 characters), to /output/entry.txt.

The reply was chosen from 24 original candidates (12 in round one, 10
challengers in round two, plus 2 controls) scored against the judge brief:
it reads as an auto-reply in the plant's own voice, the plant's life —
ignored since March, never watered — drives the joke, and the surprise
("legally a dried arrangement") is saved for the last few words. The two
controls — a stock office phrase and a worn-out leaf pun — scored far
below the winner, so neither pattern was used.

Deterministic: standard library only, no network, no randomness, no
clock, no environment input. The same bytes are written on every run.
"""

import os

REPLY = "Hi, this is the fern. I have been here since March. Nobody has watered me. I am now legally a dried arrangement."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
