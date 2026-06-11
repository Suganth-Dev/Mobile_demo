/* =====================================================
   MTS Connect - Service Worker v2 (Bulletproof)
   ===================================================== */

const CACHE_NAME = 'mts-connect-v2';

// ── Install: Skip waiting immediately, no precaching ──
self.addEventListener('install', (event) => {
  console.log('[SW] Installed v2');
  self.skipWaiting();
});

// ── Activate: Claim clients, remove old caches ────────
self.addEventListener('activate', (event) => {
  console.log('[SW] Activated v2');
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.map((key) => {
        if (key !== CACHE_NAME) {
          console.log('[SW] Removing old cache:', key);
          return caches.delete(key);
        }
      }))
    ).then(() => self.clients.claim())
  );
});

// ── Fetch: Network first, cache as backup ─────────────
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Skip cross-origin requests (fonts, CDN etc) - let browser handle them
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Only cache valid responses
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // Offline fallback: try cache, then serve index.html for navigation
        return caches.match(event.request).then((cached) => {
          if (cached) return cached;
          if (event.request.mode === 'navigate') {
            return caches.match('/Mobile_demo/index.html');
          }
        });
      })
  );
});
