from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now=True)