from django.http import HttpResponseForbidden
from django.core.cache import cache

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = f'ratelimit:{request.META["REMOTE_ADDR"]}'
        requests_made = cache.get(key, 0)

        limit = 5

        if requests_made >= limit:
            return HttpResponseForbidden('Rate limit exceeded')

        cache.set(key, requests_made + 1, timeout=3600)

        return self.get_response(request)
