from django.shortcuts import render
from functools import wraps

def user_role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.user_type in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'error404.html', status=403)
        return _wrapped_view
    return decorator
