"""smithy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from smithy import views

urlpatterns = [
    path('', include('seller.urls')),
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('get-name/', views.get_name, name='get-name'),

    path('tools/', views.tools, name='tools'),
    path('weapones/', views.weapones, name='weapones'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('utensils/', views.utensils, name='utensils'),

    path('product-details/<product_id>',
         views.product_details, name='product_details'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('delete-from-cart/', views.delete_from_cart, name='delete-from-cart'),
    path('increase_quantity/<int:item_id>/',
         views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:item_id>/',
         views.decrease_quantity, name='decrease_quantity'),
    path('payment', views.payment, name="payment"),
]
