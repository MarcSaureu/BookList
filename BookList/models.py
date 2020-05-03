 
from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    photo = models.FilePathField(path='BookList/static/img/', default='img/no_photo.png')

class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=50)
    cover_page = models.FilePathField(path='BookList/static/img/')
    synopsis = models.TextField()
    release_date = models.DateField()
    authors = models.ManyToManyField(Author)

class List(models.Model):
    books = models.ManyToManyField(Book)

class User(auth_models.AbstractUser):
    birth_date = models.DateField(null=True)
    photo = models.FilePathField(path='BookList/static/img/', default='img/no_photo.png')
    lists = models.ManyToManyField(List)
