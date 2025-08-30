// Service Worker for Islamic Study Guide PWA
const CACHE_NAME = 'islamic-study-guide-v1.0.0';
const urlsToCache = [
  '/',
  '/complete-islamic-study-guide-dark.html',
  '/islamic-study-index.html',
  '/quran-index.html',
  '/hadith-index.html',
  '/fiqh-index.html',
  '/sunnah-index.html',
  '/aqeedah-index.html',
  '/seerah-index.html',
  '/duas-index.html',
  '/ethics-index.html',
  '/history-index.html',
  '/science-index.html',
  '/prayer-worship.html',
  '/ramadan-fasting.html',
  '/hajj-umrah.html',
  '/zakat-charity.html',
  '/family-marriage.html',
  '/business-finance.html',
  '/health-medicine.html',
  '/education-learning.html',
  '/social-community.html'
];

// Install event - cache resources
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch event - serve from cache when offline
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached version or fetch from network
        return response || fetch(event.request);
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
