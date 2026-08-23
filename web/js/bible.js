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
