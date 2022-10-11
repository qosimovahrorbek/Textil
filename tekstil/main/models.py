from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS = (
        (1, 'boss'),
        (2, 'seller'),
        (3, 'warehouse'),
    )
    types = models.IntegerField(choices=STATUS, default=1)

class CategoryWear(models.Model):
    name = models.CharField(max_length = 244)

class Product(models.Model):
    name = models.CharField(max_length=244)
    category = models.ForeignKey(CategoryWear, on_delete = models.PROTECT)
    pr_amount = models.IntegerField()
    price = models.IntegerField()
    quontity = models.IntegerField(default=0)

class Order(models.Model):
    who = models.CharField(max_length=244)
    phone = models.IntegerField()
    adress = models.CharField(max_length=300)

class OrderItem(models.Model):
    who = models.ForeignKey(Order, on_delete=models.PROTECT)
    which_products = models.ManyToManyField(Product)
    total = models.IntegerField()
    date = models.DateField()
