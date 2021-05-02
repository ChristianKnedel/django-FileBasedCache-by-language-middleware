# django-FileBasedCache-by-language-middleware
Django middleware to manipulate file based cache location by  translation.


# How to install


```
$ cd project/middleware
$ wget 
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
      'LOCATION': 'cache',
      'OPTIONS': {
	    'CULL_FREQUENCY': 2,
        'MAX_ENTRIES': 50000
      }
    }
}
```

# Details
