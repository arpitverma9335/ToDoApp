var staticCacheName = 'prefetch';

self.addEventListener('install', function(event) {
event.waitUntil(
  caches.open(staticCacheName).then(function(cache) {
  return cache.addAll([
     '/static/webfonts/fa-solid-900.b75b4bfe0d58.woff2?5c7df99df232',
     '/static/CACHE/css/output.02cece9151ee.css',
     '/static/CACHE/css/output.4eedc337ee64.css',
     '/static/CACHE/css/output.5812a24c0341.css',
     '/static/CACHE/css/output.49951ffea8cb.css',
  ]);
  })
);
});

self.addEventListener("fetch", event => {
    event.respondWith(
            fetch(event.request).catch(err =>
                caches.match(event.request).then(response => response)
            )
        );
});