from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)