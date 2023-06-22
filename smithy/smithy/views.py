from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import service

def homePage(request):
    if request.method=="GET":
        output=request.GET.get('email')
    return render(request,"index.html",{'email':output})

def tools(request):
    serviceData=service.objects.all().order_by('price')
    data={
        'serviceData':serviceData
    }
    return render(request,"tools.html",data)

 

def login(request):
    user_name=''
    if request.method == "POST":
        user_name = request.POST.get('email')
        pass_word = request.POST.get('password')
        url="/?email={}".format(user_name)
        return HttpResponseRedirect(url)

    return render(request, "login.html",{'uname':user_name})


def signup(request):
    return render(request,"signup.html")