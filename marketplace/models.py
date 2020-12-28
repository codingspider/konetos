from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True, default=now)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, default=now)

    def __str__(self):
        return self.name


class ProductSlider(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='sliders/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(null=True, default=now)

    def __str__(self):
        return self.name