from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from product.models import Product
from django.contrib.auth.models import User, auth,Group
from django.contrib.auth import authenticate,login,logout
from .decorates import unauthenticated_user,allowed_user, admin_only
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from django.contrib import messages

@login_required(login_url='login')
def homePage(request):
    productData=Product.objects.all().order_by('price')
    data={
        'productData':productData
    }
    return render(request,"index.html",data)

@login_required(login_url='login')
@admin_only
def admin(request):
    return render(request,"admin_page.html")
@login_required(login_url='login')
def tools(request):
    productData=Product.objects.all().order_by('price')
    data={
        'productData':productData
    }
    return render(request,"tools.html",data)

@login_required(login_url='login')
def agriculture(request):
    productData=Product.objects.all().order_by('price')
    data={
        'productData':productData
    }
    return render(request,"agriculture.html",data)

@login_required(login_url='login')
def utensils(request):
    productData=Product.objects.all().order_by('price')
    data={
        'productData':productData
    }
    return render(request,"utensils.html",data)


@login_required(login_url='login')
def weapones(request):
    productData=Product.objects.all().order_by('price')
    data={
        'productData':productData
    }
    return render(request,"weapones.html",data)


@login_required(login_url='login')
def cart(request):
    
    return render(request,"cart.html")


@login_required(login_url='login')
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product_details': product,
        'similar_products': similar_products,
    }

    return render(request, 'product_details.html', context)



@login_required(login_url='login')
def add_to_cart(request): 
    user=request.user 
    product_id=request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    if Cart.objects.filter(user=user, product=product).exists():
        return redirect('/cart')
    Cart(user=user,product=product).save()
    return redirect('/cart')


@login_required(login_url='login')
def show_cart(request):
    user=request.user 
    cart= Cart.objects.filter(user=user)
    amount = 0
    shiping_amount = 40
    l= len(cart)
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + shiping_amount
    return render(request,'cart.html',locals())



@login_required(login_url='login')
def delete_from_cart(request):
   product_id=request.GET.get('product_id')
   Cart.objects.filter(id=product_id).delete()
   messages.success(request,"Your item deleted from cart !!")
   return HttpResponseRedirect('/cart')


def increase_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('/cart')  
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('/cart')


@login_required(login_url='shop:login')
def payment(request):
    return render(request, 'payment_page.html')





# @allowed_user
@unauthenticated_user
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


@unauthenticated_user
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


def get_name(request):
    search=request.GET.get('search')
    payload=[]
    if search:
        objs=Product.objects.filter(name__icontains=search)
        for obj in objs:
            payload.append({
                'name':obj.name
            })
    return JsonResponse({
        'status' : True ,
        'payload' : payload

    })