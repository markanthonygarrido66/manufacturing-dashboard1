from django.http import HttpResponseForbidden

def allowed_roles(roles=None):

    if roles is None:
        roles = []

    def wrapper(view_func):

        def inner(request, *args, **kwargs):

            if request.user.is_authenticated:

                if request.user.role in roles:
                    return view_func(
                        request,
                        *args,
                        **kwargs
                    )

            return HttpResponseForbidden(
                "Unauthorized Access"
            )

        return inner

    return wrapper