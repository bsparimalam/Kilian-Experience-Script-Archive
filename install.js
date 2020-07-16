var cachename = "kilianscripts_0_0_6";
const expectedCaches = [cachename];
const files2cache = [
    './',
    './icons/icon-512.png',
    './icons/icon-152.png',
    './images/background-01.png',
    './images/background-02.png',
    './images/background-03.png',
    './images/background-04.png',
    './favicon.ico',
    './index.css',
    './index.html',
    './index.js',
    './index.json'
];
self.addEventListener('install', function(event) {
  console.log(cachename + ' downloading...');
  event.waitUntil(caches.open(cachename)
    .then(function(cache) {
      cache.addAll(files2cache);
    }));
  console.log('app download complete!');
});

self.addEventListener('activate', function(event){
  console.log('app installation complete!');
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.map(key => {
        if (!expectedCaches.includes(key)) {
          return caches.delete(key);
        }
      })
    )).then(() => {
      console.log(cachename + ' ready to load offline!');
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(res) {
        if (res) {
          return res;
        } else {
          return fetch(event.request);
        }
      })
  );
});