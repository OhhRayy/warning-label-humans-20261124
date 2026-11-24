"""Warning Label for Humans: One Line, Big Laugh
(make.fun bounty u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

Writes one safety warning label to /output/entry.txt. Deterministic:
the same line, byte for byte, on every run. No network, no randomness,
no input.

The line was picked for the judge's brief: it reads like a real label
("WARNING: Contents: one human"), it is funny first and plausible second,
and every clause is a recognisable human bug — leaking feelings, heating
up in small talk, shutting down without saving.
"""

import os

LINE = (
    "WARNING: Contents: one human. May leak feelings without warning, "
    "overheat in small talk, and shut down without saving."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space.
    assert 1 <= len(text) <= 160, "line must be 1-160 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
