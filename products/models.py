from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Cart(models.Model):
    item = models.CharField(max_length=225)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    subtotal = models.IntegerField()