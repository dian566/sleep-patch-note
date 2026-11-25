#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes one patch-note line announcing that human sleep is fixed,
byte-exact, to /output/entry.txt. The line is a single line of
119 characters: inside the 1-160 gate, UTF-8, no trailing newline.
"""

import os  # only stdlib; no third-party deps

MESSAGE = "Fixed: sleep no longer ships with a 45-minute ceiling-staring loading screen. It now starts the moment your eyes close."

LIMIT = 160


def _encode(text: str) -> bytes:
    if not text or text != text.strip():
        raise SystemExit("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must fit on one line")
    if "  " in text:
        raise SystemExit("entry must not contain double spaces")
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit("entry is %d chars, gate allows 1-160" % len(text))
    data = text.encode("utf-8")
    if len(data) > LIMIT:
        raise SystemExit("entry is %d bytes, gate allows 1-160" % len(data))
    return data


def _store(data: bytes) -> str:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return path


def run() -> None:
    payload = _encode(MESSAGE)
    _store(payload)


if __name__ == "__main__":  # entry point
    run()
