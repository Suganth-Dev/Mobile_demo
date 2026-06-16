/* =====================================================
   MTS Connect - Service Worker v3
   Works on ANY host (Render, GitHub Pages, local)
   ===================================================== */

const CACHE_NAME = 'mts-connect-v16';

// ── Install: Skip waiting immediately ─────────────────
self.addEventListener('install', (event) => {
  console.log('[SW] v3 installed');
  self.skipWaiting();
});

// ── Activate: Claim clients, clean old caches ─────────
self.addEventListener('activate', (event) => {
  console.log('[SW] v3 activated');
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// ── Fetch: Network first, cache as fallback ───────────
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Only handle same-origin requests (skip CDN/fonts)
  const requestUrl = new URL(event.request.url);
  if (requestUrl.origin !== self.location.origin) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Cache valid responses
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME)
            .then(cache => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // Offline: serve from cache
        return caches.match(event.request)
          .then((cached) => {
            if (cached) return cached;
            // For page navigation, serve index.html
            if (event.request.mode === 'navigate') {
              return caches.match(self.registration.scope + 'index.html');
            }
          });
      })
  );
});
