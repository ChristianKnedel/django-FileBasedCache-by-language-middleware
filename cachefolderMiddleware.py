from django.conf import settings
from django.utils import translation

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class cachefolderMiddleware(MiddlewareMixin):

    def process_request(self, request):
        language_code = translation.get_language()
        settings.CACHES['file']['LOCATION'] = settings.CACHES_BASE_PATH + '/' + language_code
