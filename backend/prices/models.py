from django.db import models

class Price(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100, decimal_places=2)