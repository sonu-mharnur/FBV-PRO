from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.CharField(max_length=40)
    duration = models.FloatField()
