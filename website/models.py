from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    user = models.CharField(max_length = 20)
    email = models.CharField(max_length = 40)
    password = models.CharField(max_length = 20)

class Book(models.Model):
    id = models.IntegerField()
    ISBN = models.CharField(max_length = 13)
    title = models.CharField(max_length = 50)
    cover_page = models.FilePathField(path = '/img')
    synopsis = models.TextField()
    release_date = models.DateField()

class Author(models.Model):
    id = models.IntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth_date = models.DateField()
    photo = models.FilePathField(path = '/img')
