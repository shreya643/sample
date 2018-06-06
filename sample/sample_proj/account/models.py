from django.db import models

# Create your models here.

class Seller(models.Model):
    seller_name = models.CharField(max_length=30)
    seller_email = models.EmailField()
    seller_password = models.CharField(max_length=80)


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    buyer_password = models.CharField(max_length=80)


class Product(models.Model):
    name = models.CharField(max_length=80)
    stock = models.CharField(max_length=30)
    price = models.CharField(max_length=60)
    ratings = models.CharField(max_length=2)
    seller_name = models.ManyToManyField(Seller)