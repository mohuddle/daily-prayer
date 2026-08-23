#!/usr/bin/env python3
"""Sanity-check the year-repeating Tabletalk plan."""

from __future__ import annotations

import json
from calendar import monthrange
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = json.loads((ROOT / "web" / "data" / "plan.json").read_text())["days"]


def main() -> None:
    missing = [
        f"{m:02d}-{d:02d}"
        for m in range(1, 13)
        for d in range(1, monthrange(2026, m)[1] + 1)
        if f"{m:02d}-{d:02d}" not in DAYS
    ]
    assert not missing, missing
    assert "02-29" in DAYS
    assert DAYS["01-01"]["ot"] == "Genesis 1–2"
    assert DAYS["01-01"]["nt"] == "Matthew 1"
    assert DAYS["08-23"]["ot"] == "Psalm 120–125"
    assert DAYS["08-23"]["nt"] == "1 Corinthians 7"
    assert DAYS["12-31"]["nt"] == "Revelation 22"
    print("plan ok:", len(DAYS), "keys")


if __name__ == "__main__":
    main()
