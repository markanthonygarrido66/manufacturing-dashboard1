from django.contrib.auth import logout
from django.shortcuts import redirect
import time

class AutoLogoutMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            now = time.time()
            last = request.session.get("last_activity", now)

            if now - last > 900:  # 15 minutes
                from django.contrib.auth import logout
                logout(request)
                return redirect("/")

            request.session["last_activity"] = now

        return self.get_response(request)