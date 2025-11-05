from django.shortcuts import redirect
from functools import wraps

def role_required(roles_permitidos):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')

            if request.user.rol not in roles_permitidos:
                return redirect('inicio')

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
