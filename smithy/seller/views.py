from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from product.models import Product
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')


def products(request):
    productData = Product.objects.all()
    data = {
        'productData': productData
    }
    return render(request,'products.html',data)

def performance(request):
    return render(request,'performance.html')

def seller_orders(request):
    return render(request,'orders.html')

def seller_profile(request):
    return render(request,'profile.html')

def help_center(request):
    return render(request,'help_center.html')

def seller_delete(request):
    product_id = request.GET.get('product_id')
    Product.objects.filter(id=product_id).delete()
    messages.success(request, "Your item deleted from cart !!")
    return redirect('/products')


def add_products(request):
    
    if request.method == "POST":
        name = request.POST.get('pname')
        price = request.POST.get('pprice')
        discount = request.POST.get('pdiscount')
        category = request.POST.get('pcategory')
        quantity = request.POST.get('pquantity')
        image_file = request.FILES.get('pimg')
        # image_instance = 'na'
        # if 'image_file' in request.FILES:
        #     image_instance = Product(product_image = image_file)
        description = request.POST.get('pdescription')
        # print(name,price,discount,quantity,image_instance,description)
        new_product = Product.objects.create(
            name=name,
            price=price,
            discount=discount,
            quantity=quantity,
            category=category,
            product_image=image_file,
            description=description
        )
        new_product.save()
    return render(request, "add_products.html")