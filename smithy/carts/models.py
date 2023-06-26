from django.db import models
from django.contrib.auth.models import User
from service.models import service

# Create your models here.
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    

    
class cartItems(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(service,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    

