# FileBasedCache by translation
Django middleware to manipulate file based cache location by  translation.


# How to install
```
$ cd project/middleware
$ wget https://raw.githubusercontent.com/ChristianKnedel/django-FileBasedCache-by-language-middleware/main/cachefolderMiddleware.py
```

# How to use
In your settings.py file in your Django project directory, please add middleware.cachefolderMiddleware.cachefolderMiddleware to the MIDDLEWARE array.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #new:
    'django.middleware.locale.LocaleMiddleware',
    'middleware.cachefolderMiddleware.cachefolderMiddleware',
]

```
And configure caches in your app:
```
CACHES_BASE_PATH = 'cache'
CACHES = {
    'default': {
      'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
      'LOCATION': 'memcached:11211',
    },
    'database': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'cache',
      'OPTIONS': {
	    'CULL_FREQUENCY': 2,
            'MAX_ENTRIES': 200
        }
    },
    'file': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': CACHES_BASE_PATH,
      'OPTIONS': {
	    'CULL_FREQUENCY': 2,
        'MAX_ENTRIES': 50000
      }
    }
}
```

# Details / Folder structure
My cache assets folder looks like this:
- cache-folder
  - ar
    - 00a1057a3371d994771cb86bbeb02875.djcache
    -  63577b187c282b4220a8aa5c22091be3.djcache
    -  b43b2e2b2a8e9d4f908e84890cfca04a.djcache
    -  ba45ce341a32d4379e7346d631c54fe1.djcache
    -  ...
  - de
  - en
  - zh
