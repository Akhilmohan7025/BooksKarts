from django.shortcuts import redirect


def sign_in_required(fun):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return fun(request, *args, **kwargs)
        else:
            return redirect("signup")

    return wrapper

def owner_sign_in_required(fun):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return fun(request, *args, **kwargs)
        else:
            return redirect("signup")

    return wrapper


