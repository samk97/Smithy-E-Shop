from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect

def unauthenticated_user(view_fun):
    def wrapper_fun(request,*args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home')
        else:
            return view_fun(request,*args, **kwargs)
        
    return wrapper_fun

def allowed_user(allowed_roles=[]):
    def decorater(view_fun):
        def wrapper_fun(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_fun(request,*args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page !!!")
            return view_fun(request,*args, **kwargs)
        return wrapper_fun
    return decorater


def admin_only(view_fun):
    def wrapper_fun(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer' :
            return redirect('home')
        if group == 'admin' :
            return view_fun(request,*args, **kwargs)
        
    return wrapper_fun