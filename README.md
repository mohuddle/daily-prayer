# Daily Prayer

A phone-friendly daily office after Matthew Henry’s *A Method for Prayer* (1710). One sitting, any hour of the day: adoration, confession, the day’s Scripture, petitions, intercession, thanksgiving, and a close in the Lord’s Prayer.

Live site: https://mohuddle.github.io/daily-prayer/

This is a sibling of [daily-office-reader](https://github.com/mohuddle/daily-office-reader). That app follows a morning/evening lectionary. This one is a personal devotion: Henry’s heads of prayer plus a Bible-in-a-year plan.

## The office

1. **Adoration** — Henry, chapter 1
2. **Confession** — chapter 2
3. **The Word** — today’s Old and New Testament lessons
4. **Petitions** — chapter 3
5. **Intercession** — chapter 5
6. **Thanksgiving** — chapter 4
7. **Conclusion** — the Lord’s Prayer (chapter 8) and a commendation (chapter 7)

Henry meant the heads as a vocabulary, not a script. Pray the day’s reading in these shapes.

Each head has a **Prayers for …** rollup: a continuous assisting prayer for that part of the office. The wording follows Henry’s 1710 public-domain text.

**Today’s head** walks the [Method index](https://www.matthewhenry.org/read/index/) by day of year: Adoration 1.1–1.19, Confession 2.1–2.20, Petition 3.1–3.41, Thanksgiving 4.1–4.41, Intercession 5.1–5.20, Conclusion 6.1–6.5.

After the lessons, **Turn a phrase** asks you to carry a line from today’s chapters into the petitions. The note stays in the browser for that date.

**Also today** holds occasional addresses (8.x): Lord’s Day on Saturday and Sunday, a morning or evening sentence by the clock, and a drawer for a meal, a journey, sickness, or a burden. There is still one sitting, not a second office.

Thanksgiving adds **this week’s mercy** (incarnation, cross, resurrection, Spirit, Scripture, hope) by weekday. Intercession keeps a standing list for the nations, the persecuted, ministers, rulers, and the lost. Conclusion includes **Pray the Lord’s Prayer open** (Henry’s petition-by-petition paraphrase).

The full Method index and family short forms (9.x) are a lookup at `method.html`, not part of the daily sitting. 1710 state prayers are prayed as civil government, not as printed politics.

## Scripture plan

Lessons come from the [*Tabletalk* Bible reading plan](https://www.ligonier.org/posts/bible-reading-plans) (Ligonier Ministries; 2026 card, stored as calendar dates `MM-DD` so the plan repeats every year).

- Each day has one Old Testament block and one New Testament block.
- Weekend catch-up rows on the 2026 card are frozen to those dates. Both days of a pair share the same reading.
- February 29 reuses February 28.

Rebuild `web/data/plan.json` after editing the table:

```bash
python3 scripts/prepare_plan.py
```

Lessons open on [BibleGateway](https://www.biblegateway.com/) in the **NKJV**. OT and NT sit on two tabs in The Word.

## Run the PWA

From the repo root:

```bash
python3 scripts/serve_lan.py --host 0.0.0.0 --ports 8767
```

Then open http://127.0.0.1:8767/

Port **8767** sits beside Daily Office (8765) and Daily Office Reader (8766). You do not need Grok Build or an xAI key.

To keep it running after reboots:

- Linux: [LINUX.md](LINUX.md) (systemd --user)
- Windows 11: [WINDOWS.md](WINDOWS.md) (Task Scheduler)

## Credits

- Matthew Henry, *A Method for Prayer with Scripture Expressions Proper to Be Used under Each Head* (London, 1710). Public domain.
- [Ligonier Ministries, Bible reading plans](https://www.ligonier.org/posts/bible-reading-plans) — the *Tabletalk* Bible reading plan (two readings a day, Old and New Testament). Not affiliated.
- Lesson links: [BibleGateway](https://www.biblegateway.com/).
- Tab pattern inspired by [Daily Office For All](https://dailyofficeforall.com/morning-prayer.html).
