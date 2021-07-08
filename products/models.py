from django.db import models

# Create your models here.

# Product : name, weight, price, created_at, updated_at

class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()