#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

The program writes a single sentence to /output/entry.txt. The sentence
must convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. The gate allows 1 to 240 characters
of UTF-8 text, so the pitch is kept short, plain and honest: a concrete
reason to say yes tonight, and nothing to lose by trying.
"""

import os

PITCH = (
    "Describe the app idea you keep telling friends about to an AI agent "
    "on make.fun, and tap through your first working version tonight \u2014 "
    "free to try, no code to learn, and nothing to lose if you hate it."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(
            "pitch must be 1-240 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote /output/entry.txt (%d characters)" % len(text))


if __name__ == "__main__":
    main()
