from django.http import HttpResponseForbidden

def allowed_roles(roles=[]):
    def wrapper(view_func):
        def inner(request, *args, **kwargs):
            if request.user.is_authenticated:
                if hasattr(request.user, 'userprofile'):
                    if request.user.userprofile.role in roles:
                        return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("Unauthorized Access")
        return inner
    return wrapper