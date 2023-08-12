from django.contrib import admin
from seller.models import Order

# Register your models here.
class OrderModelAdmid(admin.ModelAdmin):
    list_display = ('seller','buyer', 'product', 'quantity','order_date','status','price','total_amount','transaction_id','address_line','city','state','postal_code','mob')

admin.site.register(Order, OrderModelAdmid)