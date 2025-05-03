from django.shortcuts import redirect
from django.conf import settings

EXCLUDE_PATHS = [
    '/users/login/',
    '/users/register/',
    '/users/test-login/', 
    '/admin/',
    '/static/',
    '/media/',
    '/favicon.ico',
]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Только GET, POST, и HEAD обрабатываем
        if hasattr(request, 'user') and not request.user.is_authenticated:
            path = request.path
            if not any(path.startswith(p) for p in EXCLUDE_PATHS):
                return redirect(settings.LOGIN_URL)
        return self.get_response(request)
