from audioop import reverse
import re
from statistics import mode
from unicodedata import name
from django.conf import settings
from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=180)
    image = models.ImageField()
    description = models.TextField()
    
    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=190)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class OrderProduct(models.Model):
#     product = models.ForeignKey(product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} of {self.product.name}"

# class Order (models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     products = models.ManyToManyField(OrderProduct)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
class order(models.Model):
    productid = models.IntegerField()
    user_id = models.IntegerField()
    num =models.IntegerField()
