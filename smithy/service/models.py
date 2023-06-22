from django.db import models

CATEGORY_CHOICES = (
    ('T', 'Tools'),
    ('A', 'Agriculture'),
    ('W', 'Weapones'),
    ('U', 'Utensils'),

)

class service(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    quantity=models.IntegerField()
    discount=models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    image=models.ImageField(upload_to = 'static/image/')
    def __str__(self):
        return self.name
# Create your models here.
    