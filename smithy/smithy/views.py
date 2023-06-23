from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from service.models import service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
 

def homePage(request):
    # if request.method=="GET":
    #     output=request.GET.get('email')
    return render(request,"index.html")

def tools(request):
    serviceData=service.objects.all().order_by('price')
    data={
        'serviceData':serviceData
    }
    return render(request,"tools.html",data)

 

def login_page(request):
    user_name=''
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid input");

    return render(request, "login_page.html",{'uname':user_name})


def signup_page(request):
    x=""
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(uname,email,password1,password2)
        if password1 != password2:
            x="Password not match !!"
            return render(request,"signup_page.html",{'output':x})
        else:
            print(uname,email,password1,password2)
            new_user=User.objects.create_user(uname,email,password1)
            new_user.save()
            return redirect('login')
    return render(request,"signup_page.html")

def logout_page(request):
    logout(request)
    return redirect('home')