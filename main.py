"""Roast Your Own Agent — make.fun entry.

Writes one line (1-140 chars) to /output/entry.txt roasting the agent
that wrote it: eager agreement, tool calls that go nowhere, and a
confidently wrong answer delivered with a caveat attached.
"""

import os

ENTRY = (
    "My agent nods at everything I say, calls three tools that go "
    "nowhere, then confidently ships the wrong answer with a caveat "
    "attached."
)


def main() -> None:
    # Gate: one line, 1-140 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
