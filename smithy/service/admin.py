from django.contrib import admin
from service.models import service

class toolsAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity','discount','category','image')

admin.site.register(service,toolsAdmin)
# Register your models here.
