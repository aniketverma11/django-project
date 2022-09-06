from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100)
    price =models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=100)

    