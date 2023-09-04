
from functools import wraps
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Project


def get_project(function):
    @wraps(function)
    def wrap(request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        return function(request, project, *args, **kwargs)
    return wrap

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
