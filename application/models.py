from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    quantity = models.IntegerField()