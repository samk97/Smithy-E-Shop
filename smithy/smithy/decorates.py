from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect

def unauthenticated_user(view_fun):
    def wrapper_fun(request,*args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home')
        else:
            return view_fun(request,*args, **kwargs)
        
    return wrapper_fun


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
          return redirect('home')  

        return view_func(request, *args, **kwargs)

    return wrapper