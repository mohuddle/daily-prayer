#!/usr/bin/env python3
"""Build a year-repeating Tabletalk Bible-in-a-year plan.

Source: Ligonier Tabletalk *Bible in a Year 2026* card
(2026_Tabletalk_Bible_Reading_Plan.pdf). Weekend (WE) blocks from that
card are assigned to both calendar dates they covered in 2026. The plan
is then keyed MM-DD so it repeats every year. Leap-day Feb 29 copies Feb 28.
"""

from __future__ import annotations

import json
from calendar import monthrange
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "web" / "data" / "plan.json"

# (month, day or (start, end), OT label, NT label)
# Weekend pairs are the 2026 Saturday–Sunday WE rows on the Tabletalk card.
ROWS: list[tuple[int, int | tuple[int, int], str, str]] = [
    # January — Genesis / Exodus + Matthew
    (1, 1, "Genesis 1–2", "Matthew 1"),
    (1, 2, "Genesis 3–5", "Matthew 2"),
    (1, (3, 4), "Genesis 6–10", "Matthew 3–4"),
    (1, 5, "Genesis 11–13", "Matthew 5"),
    (1, 6, "Genesis 14–16", "Matthew 6"),
    (1, 7, "Genesis 17–19", "Matthew 7"),
    (1, 8, "Genesis 20–22", "Matthew 8"),
    (1, 9, "Genesis 23–24", "Matthew 9"),
    (1, (10, 11), "Genesis 25–29", "Matthew 10"),
    (1, 12, "Genesis 30–31", "Matthew 11:1–15"),
    (1, 13, "Genesis 32–33", "Matthew 11:16–30"),
    (1, 14, "Genesis 34–35", "Matthew 12"),
    (1, 15, "Genesis 36–37", "Matthew 13:1–23"),
    (1, 16, "Genesis 38–40", "Matthew 13:24–58"),
    (1, (17, 18), "Genesis 41–46", "Matthew 14:1–21"),
    (1, 19, "Genesis 47", "Matthew 14:22–36"),
    (1, 20, "Genesis 48–49", "Matthew 15:1–28"),
    (1, 21, "Genesis 50–Exodus 1", "Matthew 15:29–16:4"),
    (1, 22, "Exodus 2–4", "Matthew 16:5–28"),
    (1, 23, "Exodus 5–6", "Matthew 17"),
    (1, (24, 25), "Exodus 7–10", "Matthew 18:1–20"),
    (1, 26, "Exodus 11–12", "Matthew 18:21–35"),
    (1, 27, "Exodus 13–16", "Matthew 19:1–15"),
    (1, 28, "Exodus 17–19", "Matthew 19:16–30"),
    (1, 29, "Exodus 20–22", "Matthew 20:1–16"),
    (1, 30, "Exodus 23–25", "Matthew 20:17–34"),
    (1, 31, "Exodus 26–28", "Matthew 21"),
    # February — the Jan 31 WE on the card is Sat Jan 31 + Sun Feb 1.
    (2, 1, "Exodus 26–28", "Matthew 21"),
    (2, 2, "Exodus 29–30", "Matthew 22:1–22"),
    (2, 3, "Exodus 31–32", "Matthew 22:23–46"),
    (2, 4, "Exodus 33–34", "Matthew 23:1–22"),
    (2, 5, "Exodus 35–36", "Matthew 23:23–39"),
    (2, 6, "Exodus 37–38", "Matthew 24:1–35"),
    (2, (7, 8), "Exodus 39–Leviticus 1", "Matthew 24:36–25:30"),
    (2, 9, "Leviticus 2–3", "Matthew 25:31–46"),
    (2, 10, "Leviticus 4–6", "Matthew 26:1–35"),
    (2, 11, "Leviticus 7–9", "Matthew 26:36–56"),
    (2, 12, "Leviticus 10–12", "Matthew 26:57–75"),
    (2, 13, "Leviticus 13–15", "Matthew 27"),
    (2, (14, 15), "Leviticus 16–18", "Matthew 28"),
    (2, 16, "Leviticus 19–20", "Mark 1"),
    (2, 17, "Leviticus 21–23", "Mark 2"),
    (2, 18, "Leviticus 24–26", "Mark 3"),
    (2, 19, "Leviticus 27–Numbers 1", "Mark 4"),
    (2, 20, "Numbers 2–3", "Mark 5:1–20"),
    (2, (21, 22), "Numbers 4–9", "Mark 5:21–43"),
    (2, 23, "Numbers 10–12", "Mark 6:1–29"),
    (2, 24, "Numbers 13–15", "Mark 6:30–56"),
    (2, 25, "Numbers 16–18", "Mark 7:1–13"),
    (2, 26, "Numbers 19–21", "Mark 7:14–37"),
    (2, 27, "Numbers 22–24", "Mark 8:1–21"),
    (2, 28, "Numbers 25–28", "Mark 8:22–9:50"),
    # March — Feb 28 WE is Sat Feb 28 + Sun Mar 1
    (3, 1, "Numbers 25–28", "Mark 8:22–9:50"),
    (3, 2, "Numbers 29–31", "Mark 10:1–34"),
    (3, 3, "Numbers 32–34", "Mark 10:35–52"),
    (3, 4, "Numbers 35–36", "Mark 11:1–14"),
    (3, 5, "Deuteronomy 1–3", "Mark 11:15–33"),
    (3, 6, "Deuteronomy 4–5", "Mark 12:1–27"),
    (3, (7, 8), "Deuteronomy 6–11", "Mark 12:28–13:31"),
    (3, 9, "Deuteronomy 12–13", "Mark 13:32–14:9"),
    (3, 10, "Deuteronomy 14–16", "Mark 14:10–31"),
    (3, 11, "Deuteronomy 17–19", "Mark 14:32–52"),
    (3, 12, "Deuteronomy 20–22", "Mark 14:53–72"),
    (3, 13, "Deuteronomy 23–25", "Mark 15:1–20"),
    (3, (14, 15), "Deuteronomy 26–31", "Mark 15:21–16:20"),
    (3, 16, "Deuteronomy 32–33", "Luke 1:1–38"),
    (3, 17, "Deuteronomy 34", "Luke 1:39–56"),
    (3, 18, "Joshua 1–2", "Luke 1:57–80"),
    (3, 19, "Joshua 3–4", "Luke 2:1–21"),
    (3, 20, "Joshua 5–6", "Luke 2:22–52"),
    (3, (21, 22), "Joshua 7–10", "Luke 3"),
    (3, 23, "Joshua 11–12", "Luke 4:1–41"),
    (3, 24, "Joshua 13–14", "Luke 4:42–5:26"),
    (3, 25, "Joshua 15–17", "Luke 5:27–39"),
    (3, 26, "Joshua 18–19", "Luke 6:1–26"),
    (3, 27, "Joshua 20–22", "Luke 6:27–49"),
    (3, (28, 29), "Joshua 23–Judges 3", "Luke 7:1–8:3"),
    (3, 30, "Judges 4–5", "Luke 8:4–39"),
    (3, 31, "Judges 6–7", "Luke 8:40–56"),
    # April
    (4, 1, "Judges 8–10", "Luke 9:1–27"),
    (4, 2, "Judges 11–12", "Luke 9:28–62"),
    (4, 3, "Judges 13–14", "Luke 10:1–24"),
    (4, (4, 5), "Judges 15–19", "Luke 10:25–11:36"),
    (4, 6, "Judges 20–21", "Luke 11:37–12:3"),
    (4, 7, "Ruth 1–2", "Luke 12:4–34"),
    (4, 8, "Ruth 3–4", "Luke 12:35–59"),
    (4, 9, "1 Samuel 1–2", "Luke 13:1–21"),
    (4, 10, "1 Samuel 3–6", "Luke 13:22–35"),
    (4, (11, 12), "1 Samuel 7–12", "Luke 14:1–24"),
    (4, 13, "1 Samuel 13–14", "Luke 14:25–15:10"),
    (4, 14, "1 Samuel 15–17", "Luke 15:11–32"),
    (4, 15, "1 Samuel 18–19", "Luke 16:1–13"),
    (4, 16, "1 Samuel 20–21", "Luke 16:14–31"),
    (4, 17, "1 Samuel 22–23", "Luke 17:1–19"),
    (4, (18, 19), "1 Samuel 24–28", "Luke 17:20–18:34"),
    (4, 20, "1 Samuel 29–31", "Luke 18:35–19:10"),
    (4, 21, "2 Samuel 1–3", "Luke 19:11–27"),
    (4, 22, "2 Samuel 4–5", "Luke 19:28–48"),
    (4, 23, "2 Samuel 6–8", "Luke 20:1–26"),
    (4, 24, "2 Samuel 9–11", "Luke 20:27–47"),
    (4, (25, 26), "2 Samuel 12–16", "Luke 21"),
    (4, 27, "2 Samuel 17–19", "Luke 22:1–23"),
    (4, 28, "2 Samuel 20–22", "Luke 22:24–38"),
    (4, 29, "2 Samuel 23–1 Kings 1", "Luke 22:39–71"),
    (4, 30, "1 Kings 2–3", "Luke 23:1–25"),
    # May
    (5, 1, "1 Kings 4–5", "Luke 23:26–43"),
    (5, (2, 3), "1 Kings 6–10", "Luke 23:44–24:12"),
    (5, 4, "1 Kings 11–12", "Luke 24:13–35"),
    (5, 5, "1 Kings 13–14", "Luke 24:36–53"),
    (5, 6, "1 Kings 15–16", "John 1"),
    (5, 7, "1 Kings 17–18", "John 2"),
    (5, 8, "1 Kings 19–20", "John 3:1–21"),
    (5, (9, 10), "1 Kings 21–2 Kings 4", "John 3:22–4:42"),
    (5, 11, "2 Kings 5–6", "John 4:43–54"),
    (5, 12, "2 Kings 7–9", "John 5:1–29"),
    (5, 13, "2 Kings 10–11", "John 5:30–47"),
    (5, 14, "2 Kings 12–14", "John 6:1–21"),
    (5, 15, "2 Kings 15–17", "John 6:22–59"),
    (5, (16, 17), "2 Kings 18–22", "John 6:60–7:36"),
    (5, 18, "2 Kings 23–24", "John 7:37–52"),
    (5, 19, "2 Kings 25–1 Chronicles 2", "John 7:53–8:11"),
    (5, 20, "1 Chronicles 3–5", "John 8:12–38"),
    (5, 21, "1 Chronicles 6–7", "John 8:39–59"),
    (5, 22, "1 Chronicles 8–10", "John 9:1–23"),
    (5, (23, 24), "1 Chronicles 11–14", "John 9:24–10:21"),
    (5, 25, "1 Chronicles 15–17", "John 10:22–42"),
    (5, 26, "1 Chronicles 18–20", "John 11:1–27"),
    (5, 27, "1 Chronicles 21–23", "John 11:28–44"),
    (5, 28, "1 Chronicles 24–26", "John 11:45–57"),
    (5, 29, "1 Chronicles 27–29", "John 12:1–19"),
    (5, (30, 31), "2 Chronicles 1–6", "John 12:20–13:20"),
    # June
    (6, 1, "2 Chronicles 7–9", "John 13:21–14:14"),
    (6, 2, "2 Chronicles 10–12", "John 14:15–31"),
    (6, 3, "2 Chronicles 13–15", "John 15:1–17"),
    (6, 4, "2 Chronicles 16–18", "John 15:18–16:15"),
    (6, 5, "2 Chronicles 19–22", "John 16:16–33"),
    (6, (6, 7), "2 Chronicles 23–27", "John 17"),
    (6, 8, "2 Chronicles 28–30", "John 18"),
    (6, 9, "2 Chronicles 31–33", "John 19:1–16a"),
    (6, 10, "2 Chronicles 34–36", "John 19:16b–42"),
    (6, 11, "Ezra 1–2", "John 20"),
    (6, 12, "Ezra 3–5", "John 21"),
    (6, (13, 14), "Ezra 6–10", "Acts 1:1–2:13"),
    (6, 15, "Nehemiah 1–3", "Acts 2:14–41"),
    (6, 16, "Nehemiah 4–5", "Acts 2:42–3:10"),
    (6, 17, "Nehemiah 6–8", "Acts 3:11–4:22"),
    (6, 18, "Nehemiah 9–11", "Acts 4:23–37"),
    (6, 19, "Nehemiah 12–13", "Acts 5:1–16"),
    (6, (20, 21), "Esther 1–6", "Acts 5:17–6:7"),
    (6, 22, "Esther 7–9", "Acts 6:8–7:22"),
    (6, 23, "Esther 10–Job 2", "Acts 7:23–34"),
    (6, 24, "Job 3–6", "Acts 7:35–8:3"),
    (6, 25, "Job 7–9", "Acts 8:4–25"),
    (6, 26, "Job 10–12", "Acts 8:26–40"),
    (6, (27, 28), "Job 13–17", "Acts 9:1–31"),
    (6, 29, "Job 18–20", "Acts 9:32–10:8"),
    (6, 30, "Job 21–23", "Acts 10:9–48"),
    # July — Job / Psalms + Acts / Romans
    (7, 1, "Job 24–25", "Acts 11"),
    (7, 2, "Job 26–27", "Acts 12"),
    (7, 3, "Job 28–30", "Acts 13"),
    (7, (4, 5), "Job 31–36", "Acts 14"),
    (7, 6, "Job 37–38", "Acts 15"),
    (7, 7, "Job 39–40", "Acts 16:1–15"),
    (7, 8, "Job 41–Psalm 1", "Acts 16:16–40"),
    (7, 9, "Psalm 2–3", "Acts 17:1–15"),
    (7, 10, "Psalm 4–6", "Acts 17:16–34"),
    (7, (11, 12), "Psalm 7–12", "Acts 18"),
    (7, 13, "Psalm 13–15", "Acts 19"),
    (7, 14, "Psalm 16–18", "Acts 20:1–16"),
    (7, 15, "Psalm 19–22", "Acts 20:17–38"),
    (7, 16, "Psalm 23–24", "Acts 21:1–16"),
    (7, 17, "Psalm 25–27", "Acts 21:17–36"),
    (7, (18, 19), "Psalm 28–32", "Acts 21:37–23:11"),
    (7, 20, "Psalm 33–35", "Acts 23:12–35"),
    (7, 21, "Psalm 36–38", "Acts 24"),
    (7, 22, "Psalm 39–41", "Acts 25"),
    (7, 23, "Psalm 42–43", "Acts 26"),
    (7, 24, "Psalm 44–46", "Acts 27:1–26"),
    (7, (25, 26), "Psalm 47–52", "Acts 27:27–28:10"),
    (7, 27, "Psalm 53–55", "Acts 28:11–31"),
    (7, 28, "Psalm 56–58", "Romans 1"),
    (7, 29, "Psalm 59–61", "Romans 2"),
    (7, 30, "Psalm 62–64", "Romans 3"),
    (7, 31, "Psalm 65–67", "Romans 4"),
    # August
    (8, (1, 2), "Psalm 68–72", "Romans 5"),
    (8, 3, "Psalm 73–74", "Romans 6"),
    (8, 4, "Psalm 75–76", "Romans 7"),
    (8, 5, "Psalm 77–79", "Romans 8"),
    (8, 6, "Psalm 80–84", "Romans 9:1–10:4"),
    (8, 7, "Psalm 85–87", "Romans 10:5–21"),
    (8, (8, 9), "Psalm 88–93", "Romans 11"),
    (8, 10, "Psalm 94–95", "Romans 12"),
    (8, 11, "Psalm 96–98", "Romans 13"),
    (8, 12, "Psalm 99–101", "Romans 14"),
    (8, 13, "Psalm 102–104", "Romans 15:1–21"),
    (8, 14, "Psalm 105–106", "Romans 15:22–33"),
    (8, (15, 16), "Psalm 107–110", "Romans 16–1 Corinthians 1"),
    (8, 17, "Psalm 111–112", "1 Corinthians 2"),
    (8, 18, "Psalm 113–115", "1 Corinthians 3"),
    (8, 19, "Psalm 116–119:48", "1 Corinthians 4"),
    (8, 20, "Psalm 119:49–104", "1 Corinthians 5"),
    (8, 21, "Psalm 119:105–176", "1 Corinthians 6"),
    (8, (22, 23), "Psalm 120–125", "1 Corinthians 7"),
    (8, 24, "Psalm 126–127", "1 Corinthians 8"),
    (8, 25, "Psalm 128–130", "1 Corinthians 9"),
    (8, 26, "Psalm 131–133", "1 Corinthians 10:1–22"),
    (8, 27, "Psalm 134–137", "1 Corinthians 10:23–11:1"),
    (8, 28, "Psalm 138–141", "1 Corinthians 11:2–16"),
    (8, (29, 30), "Psalm 142–145", "1 Corinthians 11:17–12:11"),
    (8, 31, "Psalm 146–148", "1 Corinthians 12:12–31"),
    # September
    (9, 1, "Psalm 149–Proverbs 1", "1 Corinthians 13"),
    (9, 2, "Proverbs 2–4", "1 Corinthians 14"),
    (9, 3, "Proverbs 5–6", "1 Corinthians 15:1–34"),
    (9, 4, "Proverbs 7–8", "1 Corinthians 15:35–58"),
    (9, (5, 6), "Proverbs 9–12", "1 Corinthians 16–2 Corinthians 1"),
    (9, 7, "Proverbs 13–14", "2 Corinthians 2"),
    (9, 8, "Proverbs 15–16", "2 Corinthians 3"),
    (9, 9, "Proverbs 17–18", "2 Corinthians 4"),
    (9, 10, "Proverbs 19–20", "2 Corinthians 5:1–6:13"),
    (9, 11, "Proverbs 21–22", "2 Corinthians 6:14–7:1"),
    (9, (12, 13), "Proverbs 23–28", "2 Corinthians 7:2–8:24"),
    (9, 14, "Proverbs 29–30", "2 Corinthians 9"),
    (9, 15, "Proverbs 31–Ecclesiastes 2", "2 Corinthians 10"),
    (9, 16, "Ecclesiastes 3–4", "2 Corinthians 11:1–15"),
    (9, 17, "Ecclesiastes 5–6", "2 Corinthians 11:16–33"),
    (9, 18, "Ecclesiastes 7–9", "2 Corinthians 12"),
    (9, (19, 20), "Ecclesiastes 10–Song of Solomon 3", "2 Corinthians 13–Galatians 1"),
    (9, 21, "Song of Solomon 4–6", "Galatians 2"),
    (9, 22, "Song of Solomon 7–Isaiah 1", "Galatians 3"),
    (9, 23, "Isaiah 2–3", "Galatians 4"),
    (9, 24, "Isaiah 4–6", "Galatians 5"),
    (9, 25, "Isaiah 7–9", "Galatians 6"),
    (9, (26, 27), "Isaiah 10–14", "Ephesians 1–2"),
    (9, 28, "Isaiah 15–17", "Ephesians 3"),
    (9, 29, "Isaiah 18–20", "Ephesians 4"),
    (9, 30, "Isaiah 21–23", "Ephesians 5"),
    # October
    (10, 1, "Isaiah 24–26", "Ephesians 6"),
    (10, 2, "Isaiah 27–28", "Philippians 1"),
    (10, (3, 4), "Isaiah 29–32", "Philippians 2–3"),
    (10, 5, "Isaiah 33–34", "Philippians 4"),
    (10, 6, "Isaiah 35–37", "Colossians 1:1–2:5"),
    (10, 7, "Isaiah 38–40", "Colossians 2:6–3:17"),
    (10, 8, "Isaiah 41–42", "Colossians 3:18–4:18"),
    (10, 9, "Isaiah 43–44", "1 Thessalonians 1"),
    (10, (10, 11), "Isaiah 45–50", "1 Thessalonians 2:1–3:5"),
    (10, 12, "Isaiah 51–53", "1 Thessalonians 3:6–13"),
    (10, 13, "Isaiah 54–55", "1 Thessalonians 4"),
    (10, 14, "Isaiah 56–58", "1 Thessalonians 5"),
    (10, 15, "Isaiah 59–61", "2 Thessalonians 1"),
    (10, 16, "Isaiah 62–64", "2 Thessalonians 2"),
    (10, (17, 18), "Isaiah 65–Jeremiah 3", "2 Thessalonians 3–1 Timothy 1"),
    (10, 19, "Jeremiah 4–5", "1 Timothy 2"),
    (10, 20, "Jeremiah 6–7", "1 Timothy 3"),
    (10, 21, "Jeremiah 8–9", "1 Timothy 4"),
    (10, 22, "Jeremiah 10–11", "1 Timothy 5:1–6:2a"),
    (10, 23, "Jeremiah 12–13", "1 Timothy 6:2b–21"),
    (10, (24, 25), "Jeremiah 14–17", "2 Timothy 1–2"),
    (10, 26, "Jeremiah 18–20", "2 Timothy 3"),
    (10, 27, "Jeremiah 21–23", "2 Timothy 4"),
    (10, 28, "Jeremiah 24–26", "Titus 1"),
    (10, 29, "Jeremiah 27–28", "Titus 2"),
    (10, 30, "Jeremiah 29–30", "Titus 3"),
    (10, 31, "Jeremiah 31–36", "Philemon–Hebrews 1"),
    # November — Oct 31 WE is Sat Oct 31 + Sun Nov 1
    (11, 1, "Jeremiah 31–36", "Philemon–Hebrews 1"),
    (11, 2, "Jeremiah 37–38", "Hebrews 2"),
    (11, 3, "Jeremiah 39–41", "Hebrews 3:1–4:13"),
    (11, 4, "Jeremiah 42–43", "Hebrews 4:14–5:10"),
    (11, 5, "Jeremiah 44–45", "Hebrews 5:11–6:12"),
    (11, 6, "Jeremiah 46–48", "Hebrews 6:13–7:10"),
    (11, (7, 8), "Jeremiah 49–Lamentations 2", "Hebrews 7:11–28"),
    (11, 9, "Lamentations 3–4", "Hebrews 8"),
    (11, 10, "Lamentations 5–Ezekiel 1", "Hebrews 9"),
    (11, 11, "Ezekiel 2–3", "Hebrews 10"),
    (11, 12, "Ezekiel 4–6", "Hebrews 11:1–16"),
    (11, 13, "Ezekiel 7–9", "Hebrews 11:17–40"),
    (11, (14, 15), "Ezekiel 10–14", "Hebrews 12–13"),
    (11, 16, "Ezekiel 15–17", "James 1"),
    (11, 17, "Ezekiel 18–20", "James 2"),
    (11, 18, "Ezekiel 21", "James 3"),
    (11, 19, "Ezekiel 22–24", "James 4"),
    (11, 20, "Ezekiel 25–26", "James 5"),
    (11, (21, 22), "Ezekiel 27–29", "1 Peter 1–2"),
    (11, 23, "Ezekiel 30–31", "1 Peter 3"),
    (11, 24, "Ezekiel 32–34", "1 Peter 4"),
    (11, 25, "Ezekiel 35–36", "1 Peter 5"),
    (11, 26, "Ezekiel 37–38", "2 Peter 1"),
    (11, 27, "Ezekiel 39–40", "2 Peter 2"),
    (11, (28, 29), "Ezekiel 41–44", "2 Peter 3–1 John 1"),
    (11, 30, "Ezekiel 45–46", "1 John 2"),
    # December
    (12, 1, "Ezekiel 47–48", "1 John 3"),
    (12, 2, "Daniel 1–2", "1 John 4"),
    (12, 3, "Daniel 3–4", "1 John 5"),
    (12, 4, "Daniel 5–6", "2 John"),
    (12, (5, 6), "Daniel 7–12", "3 John–Jude"),
    (12, 7, "Hosea 1–2", "Revelation 1"),
    (12, 8, "Hosea 3–4", "Revelation 2"),
    (12, 9, "Hosea 5–6", "Revelation 3"),
    (12, 10, "Hosea 7–10", "Revelation 4"),
    (12, 11, "Hosea 11–14", "Revelation 5"),
    (12, (12, 13), "Joel–Amos 3", "Revelation 6"),
    (12, 14, "Amos 4–6", "Revelation 7"),
    (12, 15, "Amos 7–9", "Revelation 8"),
    (12, 16, "Obadiah–Jonah 3", "Revelation 9"),
    (12, 17, "Jonah 4–Micah 2", "Revelation 10"),
    (12, 18, "Micah 3", "Revelation 11"),
    (12, (19, 20), "Micah 4–Nahum 1", "Revelation 12"),
    (12, 21, "Nahum 2–3", "Revelation 13"),
    (12, 22, "Habakkuk 1–2", "Revelation 14"),
    (12, 23, "Habakkuk 3–Zephaniah 2", "Revelation 15"),
    (12, 24, "Zephaniah 3–Haggai 2", "Revelation 16"),
    (12, 25, "Zechariah 1–3", "Revelation 17"),
    (12, (26, 27), "Zechariah 4–9", "Revelation 18"),
    (12, 28, "Zechariah 10–12", "Revelation 19"),
    (12, 29, "Zechariah 13–14", "Revelation 20"),
    (12, 30, "Malachi 1–2", "Revelation 21"),
    (12, 31, "Malachi 3–4", "Revelation 22"),
]


def expand() -> dict[str, dict]:
    days: dict[str, dict] = {}
    for month, day, ot, nt in ROWS:
        if isinstance(day, tuple):
            start, end = day
            span = list(range(start, end + 1))
            weekend = True
        else:
            span = [day]
            weekend = False
        for d in span:
            key = f"{month:02d}-{d:02d}"
            if key in days:
                raise SystemExit(f"duplicate {key}")
            days[key] = {
                "ot": ot,
                "nt": nt,
                "weekend": weekend or key in {"01-31", "02-01", "02-28", "03-01", "10-31", "11-01"},
            }
    # Leap day reuses Feb 28.
    days["02-29"] = {**days["02-28"], "leap": True}
    return days


def main() -> None:
    days = expand()
    expected = sum(monthrange(2026, m)[1] for m in range(1, 13))
    non_leap = [k for k in days if k != "02-29"]
    if len(non_leap) != expected:
        missing = [
            f"{m:02d}-{d:02d}"
            for m in range(1, 13)
            for d in range(1, monthrange(2026, m)[1] + 1)
            if f"{m:02d}-{d:02d}" not in days
        ]
        raise SystemExit(f"expected {expected} days, got {len(non_leap)}; missing {missing[:20]}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "meta": {
            "title": "Bible in a Year",
            "source": "Tabletalk magazine Bible in a Year card (Ligonier), 2026 edition",
            "description": (
                "Old Testament and New Testament readings for each calendar date. "
                "Weekend catch-up blocks from the 2026 card are frozen to those "
                "MM-DD dates so the plan repeats every year. February 29 reuses February 28."
            ),
            "tracks": ["ot", "nt"],
        },
        "days": days,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(days)} keys)")


if __name__ == "__main__":
    main()
