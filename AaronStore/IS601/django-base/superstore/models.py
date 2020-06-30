from django.db import models
class AaronGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    state = models.TextField()
