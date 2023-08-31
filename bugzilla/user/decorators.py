from functools import wraps
from django.shortcuts import get_object_or_404
from .models import User




def get_user(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = get_object_or_404(User, pk=user_pk)
        return view_func(request, user, *args, **kwargs)
    return wrap