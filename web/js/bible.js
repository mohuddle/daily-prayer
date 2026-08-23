const VERSION = "NKJV";
const GATEWAY = "https://www.biblegateway.com/passage/";

/** Turn a Tabletalk label into a BibleGateway search string. */
function gatewaySearch(label) {
  let text = String(label || "").replaceAll("–", "-").replaceAll("—", "-").trim();
  text = text.replace(/^Psalms\b/, "Psalm");
  text = text.replace(/\bPsalms\b/g, "Psalm");
  // Cross-book ranges read better as two passages.
  text = text
    .replace(/\bGenesis 50-Exodus 1\b/, "Genesis 50; Exodus 1")
    .replace(/\bExodus 39-Leviticus 1\b/, "Exodus 39-40; Leviticus 1")
    .replace(/\bLeviticus 27-Numbers 1\b/, "Leviticus 27; Numbers 1")
    .replace(/\bJoshua 23-Judges 3\b/, "Joshua 23-24; Judges 1-3")
    .replace(/\b2 Samuel 23-1 Kings 1\b/, "2 Samuel 23-24; 1 Kings 1")
    .replace(/\b1 Kings 21-2 Kings 4\b/, "1 Kings 21-22; 2 Kings 1-4")
    .replace(/\b2 Kings 25-1 Chronicles 2\b/, "2 Kings 25; 1 Chronicles 1-2")
    .replace(/\bEsther 10-Job 2\b/, "Esther 10; Job 1-2")
    .replace(/\bJob 41-Psalm 1\b/, "Job 41-42; Psalm 1")
    .replace(/\bPsalm 149-Proverbs 1\b/, "Psalm 149-150; Proverbs 1")
    .replace(/\bProverbs 31-Ecclesiastes 2\b/, "Proverbs 31; Ecclesiastes 1-2")
    .replace(/\bEcclesiastes 10-Song of Solomon 3\b/, "Ecclesiastes 10-12; Song of Solomon 1-3")
    .replace(/\bSong of Solomon 7-Isaiah 1\b/, "Song of Solomon 7-8; Isaiah 1")
    .replace(/\bIsaiah 65-Jeremiah 3\b/, "Isaiah 65-66; Jeremiah 1-3")
    .replace(/\bJeremiah 49-Lamentations 2\b/, "Jeremiah 49-52; Lamentations 1-2")
    .replace(/\bLamentations 5-Ezekiel 1\b/, "Lamentations 5; Ezekiel 1")
    .replace(/\bRomans 16-1 Corinthians 1\b/, "Romans 16; 1 Corinthians 1")
    .replace(/\b1 Corinthians 16-2 Corinthians 1\b/, "1 Corinthians 16; 2 Corinthians 1")
    .replace(/\b2 Corinthians 13-Galatians 1\b/, "2 Corinthians 13; Galatians 1")
    .replace(/\b2 Thessalonians 3-1 Timothy 1\b/, "2 Thessalonians 3; 1 Timothy 1")
    .replace(/\bPhilemon-Hebrews 1\b/, "Philemon 1; Hebrews 1")
    .replace(/\b2 Peter 3-1 John 1\b/, "2 Peter 3; 1 John 1")
    .replace(/\b3 John-Jude\b/, "3 John 1; Jude 1")
    .replace(/\bJoel-Amos 3\b/, "Joel 1-3; Amos 1-3")
    .replace(/\bObadiah-Jonah 3\b/, "Obadiah 1; Jonah 1-3")
    .replace(/\bJonah 4-Micah 2\b/, "Jonah 4; Micah 1-2")
    .replace(/\bMicah 4-Nahum 1\b/, "Micah 4-7; Nahum 1")
    .replace(/\bHabakkuk 3-Zephaniah 2\b/, "Habakkuk 3; Zephaniah 1-2")
    .replace(/\bZephaniah 3-Haggai 2\b/, "Zephaniah 3; Haggai 1-2");
  return text;
}

function gatewayUrl(label) {
  const search = gatewaySearch(label);
  const params = new URLSearchParams({
    search,
    version: VERSION,
  });
  return `${GATEWAY}?${params.toString()}`;
}

const ABBREV = {
  Gen: "Genesis", Exod: "Exodus", Lev: "Leviticus", Num: "Numbers",
  Deut: "Deuteronomy", Josh: "Joshua", Judg: "Judges", Ruth: "Ruth",
  "1 Sam": "1 Samuel", "2 Sam": "2 Samuel", "1 Kgs": "1 Kings", "2 Kgs": "2 Kings",
  "1 Chr": "1 Chronicles", "2 Chr": "2 Chronicles", Ezra: "Ezra", Neh: "Nehemiah",
  Esth: "Esther", Job: "Job", Ps: "Psalm", Psalm: "Psalm", Psalms: "Psalm",
  Prov: "Proverbs", Eccl: "Ecclesiastes", Song: "Song of Solomon", Isa: "Isaiah",
  Jer: "Jeremiah", Lam: "Lamentations", Ezek: "Ezekiel", Dan: "Daniel",
  Hos: "Hosea", Joel: "Joel", Amos: "Amos", Obad: "Obadiah", Jonah: "Jonah",
  Mic: "Micah", Nah: "Nahum", Hab: "Habakkuk", Zeph: "Zephaniah", Hag: "Haggai",
  Zech: "Zechariah", Mal: "Malachi", Matt: "Matthew", Mark: "Mark", Luke: "Luke",
  John: "John", Acts: "Acts", Rom: "Romans", "1 Cor": "1 Corinthians",
  "2 Cor": "2 Corinthians", Gal: "Galatians", Eph: "Ephesians", Phil: "Philippians",
  Col: "Colossians", "1 Thess": "1 Thessalonians", "2 Thess": "2 Thessalonians",
  "1 Tim": "1 Timothy", "2 Tim": "2 Timothy", Titus: "Titus", Phlm: "Philemon",
  Philemon: "Philemon", Heb: "Hebrews", Jas: "James", "1 Pet": "1 Peter",
  "2 Pet": "2 Peter", "1 John": "1 John", "2 John": "2 John", "3 John": "3 John",
  Jude: "Jude", Rev: "Revelation",
  Genesis: "Genesis", Exodus: "Exodus", Leviticus: "Leviticus", Numbers: "Numbers",
  Deuteronomy: "Deuteronomy", Joshua: "Joshua", Judges: "Judges",
  "1 Samuel": "1 Samuel", "2 Samuel": "2 Samuel", "1 Kings": "1 Kings",
  "2 Kings": "2 Kings", "1 Chronicles": "1 Chronicles", "2 Chronicles": "2 Chronicles",
  Nehemiah: "Nehemiah", Esther: "Esther", Proverbs: "Proverbs",
  Ecclesiastes: "Ecclesiastes", "Song of Solomon": "Song of Solomon",
  Isaiah: "Isaiah", Jeremiah: "Jeremiah", Lamentations: "Lamentations",
  Ezekiel: "Ezekiel", Daniel: "Daniel", Hosea: "Hosea", Obadiah: "Obadiah",
  Micah: "Micah", Nahum: "Nahum", Habakkuk: "Habakkuk", Zephaniah: "Zephaniah",
  Haggai: "Haggai", Zechariah: "Zechariah", Malachi: "Malachi", Matthew: "Matthew",
  Romans: "Romans", "1 Corinthians": "1 Corinthians", "2 Corinthians": "2 Corinthians",
  Galatians: "Galatians", Ephesians: "Ephesians", Philippians: "Philippians",
  Colossians: "Colossians", "1 Thessalonians": "1 Thessalonians",
  "2 Thessalonians": "2 Thessalonians", "1 Timothy": "1 Timothy",
  "2 Timothy": "2 Timothy", Hebrews: "Hebrews", James: "James",
  "1 Peter": "1 Peter", "2 Peter": "2 Peter", Revelation: "Revelation",
};
const ABBREV_KEYS = Object.keys(ABBREV).sort((a, b) => b.length - a.length);

function normalizeRef(ref) {
  return String(ref).replace(/[–—−]/g, "-").trim();
}

function stripAB(token) {
  return token.replace(/[abAB](?=-|$)/g, "").replace(/[abAB]$/, "");
}

function chapterCount(bible, book, chapter) {
  return Object.keys(bible[book][String(chapter)]).length;
}

function verseText(bible, book, chapter, verse) {
  const text = bible[book]?.[String(chapter)]?.[String(verse)];
  if (!text) throw new Error(`Missing ${book} ${chapter}:${verse}`);
  return text;
}

function expandSpan(bible, book, startCh, startVs, endCh, endVs) {
  const verses = [];
  for (let ch = startCh; ch <= endCh; ch += 1) {
    const first = ch === startCh && startVs ? startVs : 1;
    const last = ch === endCh && endVs ? endVs : chapterCount(bible, book, ch);
    for (let vs = first; vs <= last; vs += 1) {
      verses.push(verseText(bible, book, ch, vs));
    }
  }
  return verses;
}

function splitBook(ref) {
  const raw = normalizeRef(ref);
  for (const key of ABBREV_KEYS) {
    if (raw === key || raw.startsWith(`${key} `)) {
      return [ABBREV[key], raw.slice(key.length).trim()];
    }
  }
  throw new Error(`Unknown book in reference: ${ref}`);
}

function parseNumericParts(bible, book, rest) {
  const parts = rest.split(",").map((p) => p.trim()).filter(Boolean);
  const verses = [];
  let lastChapter = null;
  for (const rawPart of parts) {
    const part = stripAB(rawPart.replace(/\s+/g, ""));
    let m;
    if ((m = part.match(/^(\d+):(\d+)-(\d+):(\d+)$/))) {
      verses.push(...expandSpan(bible, book, +m[1], +m[2], +m[3], +m[4]));
      lastChapter = +m[3];
    } else if ((m = part.match(/^(\d+)-(\d+):(\d+)-(\d+)$/))) {
      verses.push(...expandSpan(bible, book, +m[1], null, +m[2], +m[4]));
      lastChapter = +m[2];
    } else if ((m = part.match(/^(\d+)-(\d+):(\d+)$/))) {
      verses.push(...expandSpan(bible, book, +m[1], null, +m[2], +m[3]));
      lastChapter = +m[2];
    } else if ((m = part.match(/^(\d+):(\d+)-(\d+)$/))) {
      verses.push(...expandSpan(bible, book, +m[1], +m[2], +m[1], +m[3]));
      lastChapter = +m[1];
    } else if ((m = part.match(/^(\d+):(\d+)$/))) {
      verses.push(...expandSpan(bible, book, +m[1], +m[2], +m[1], +m[2]));
      lastChapter = +m[1];
    } else if ((m = part.match(/^(\d+)-(\d+)$/))) {
      if (
        lastChapter != null
        && +m[1] <= chapterCount(bible, book, lastChapter)
        && +m[2] <= chapterCount(bible, book, lastChapter)
      ) {
        verses.push(...expandSpan(bible, book, lastChapter, +m[1], lastChapter, +m[2]));
      } else {
        verses.push(...expandSpan(bible, book, +m[1], null, +m[2], null));
        lastChapter = +m[2];
      }
    } else if ((m = part.match(/^(\d+)$/))) {
      if (lastChapter != null && +m[1] <= chapterCount(bible, book, lastChapter)) {
        verses.push(...expandSpan(bible, book, lastChapter, +m[1], lastChapter, +m[1]));
      } else {
        verses.push(...expandSpan(bible, book, +m[1], null, +m[1], null));
        lastChapter = +m[1];
      }
    } else {
      throw new Error(`Cannot parse ${rawPart} in ${book} ${rest}`);
    }
  }
  return verses;
}

/** BSB text for a citation such as "Psalm 51:1, 10" or "John 16:23; 14:6". */
function versesFromRef(bible, ref) {
  const chunks = [];
  let lastBook = null;
  for (const rawPart of normalizeRef(ref).split(";")) {
    let part = rawPart.trim();
    if (!part) continue;
    if (/^\d+:\d/.test(part) && lastBook) part = `${lastBook} ${part}`;
    const [book, rest] = splitBook(part);
    lastBook = book;
    chunks.push(...parseNumericParts(bible, book, rest));
  }
  if (!chunks.length) throw new Error(`No verses for ${ref}`);
  return chunks.join(" ");
}
