const CACHE = "daily-prayer-v7";
const ASSETS = [
  "./",
  "./index.html",
  "./method.html",
  "./styles.css",
  "./js/app.js",
  "./js/bible.js",
  "./js/lookup.js",
  "./data/plan.json",
  "./data/method.json",
  "./data/heads.json",
  "./data/occasional.json",
  "./data/extras.json",
  "./icons/icon.svg",
  "./manifest.webmanifest",
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(ASSETS)));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key)))
    )
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  event.respondWith(
    caches.match(req).then((cached) => {
      const fresh = fetch(req)
        .then((res) => {
          if (res.ok && new URL(req.url).origin === location.origin) {
            const copy = res.clone();
            caches.open(CACHE).then((cache) => cache.put(req, copy));
          }
          return res;
        })
        .catch(() => cached);
      return cached || fresh;
    })
  );
});
