
from functools import wraps
from django.shortcuts import get_object_or_404
from .models import Project

def get_project(function):
    @wraps(function)
    def wrap(request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        return function(request, project, *args, **kwargs)
    return wrap
