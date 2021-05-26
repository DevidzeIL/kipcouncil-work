from django.http import HttpResponse
from django.shortcuts import redirect



def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_not_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('main')
    return wrapper_func



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('У вас нет полномочий зайти сюда')
        return wrapper_func
    return decorator



def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func