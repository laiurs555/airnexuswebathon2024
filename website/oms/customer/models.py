from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_lenght=255)

class Customer(models.Model):
    name = models.CharField(max_lenght=20)
    image_url = models.CharField(max_lenght=2083)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    charges = models.FloatField()
    service_requested = models.CharField(max_length=50)
    subscription_type = models.CharField(max_length=20)

    
