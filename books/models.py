from django.db import models

# Create your models here.
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField();   
    country = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author)
    publisher = models.CharField(max_length=100)
    publishdate = models.DateField()
    price = models.FloatField();