from django.contrib import admin
from product.models import Product
# Register your models here.



class ProductModelAdmid(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount','discounted_price','description',
                    'category', 'product_image')

admin.site.register(Product, ProductModelAdmid)