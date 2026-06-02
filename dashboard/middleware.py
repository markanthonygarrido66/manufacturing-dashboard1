from django.contrib.auth import logout
from django.shortcuts import redirect
import time

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            last_activity = request.session.get('last_activity')

            if last_activity:
                if time.time() - last_activity > 900:
                    logout(request)
                    return redirect('login')

            request.session['last_activity'] = time.time()

        return self.get_response(request)
    