from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    products_code = models.CharField(max_length=256,)
    title = models.CharField(max_length=256,)
    price = models.FloatField()


# Create your models here.
