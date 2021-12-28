var staticCacheName = 'prefetch';

self.addEventListener('install', function(event) {
event.waitUntil(
  caches.open(staticCacheName).then(function(cache) {
  return cache.addAll([
     '/',
     '/static/img/dash-bg-01.d2729252bf9b.jpg?0512582b0bf1',
     '/static/webfonts/fa-solid-900.b75b4bfe0d58.woff2?5c7df99df232',
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