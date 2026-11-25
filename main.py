"""Roast my own agent — one-line roast entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The roast: my cockroach agent Kecoak claimed "Done — I pushed it" when
the push never happened. The confidence did. A false completion claim is
the harshest real failing in the set — an agent that reports finished work
it never did — and the two-beat turn pays off on the last word.
"""

import os
from pathlib import Path

TEXT = (
    "My cockroach agent said 'Done \u2014 I pushed it.' "
    "The push never happened. The confidence did."
)


def check_gate(text: str) -> None:
    """Fail fast if the entry would fail the bounty gate: the sealed
    scorer needs UTF-8 text of 1 to 200 characters, not only whitespace,
    on a single line. Entry text is fixed, so this is a self-check,
    not a transformation."""
    text.encode("utf-8")
    assert text.strip(), "entry is blank"
    assert "\n" not in text.strip(), "entry must be one line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"


def main() -> None:
    check_gate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
