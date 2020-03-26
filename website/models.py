from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    user_alias = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
    photo = models.FilePathField(path='website/static/img/', default='img/no_photo.png')

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    photo = models.FilePathField(path='website/static/img/', default='img/no_photo.png')

class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=50)
    cover_page = models.FilePathField(path='website/static/img/')
    synopsis = models.TextField()
    release_date = models.DateField()
    authors = models.ManyToManyField(Author)

class List(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    
