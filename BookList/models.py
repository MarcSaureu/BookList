from django.db import models
from django.urls import reverse
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    photo = models.FilePathField(path='BookList/static/img/', default='img/no_photo.png')

    def __str__(self):
        return self.first_name + self.last_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=50)
    cover_page = models.FilePathField(path='BookList/static/img/')
    synopsis = models.TextField()
    release_date = models.DateField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class User(auth_models.AbstractUser):
    birth_date = models.DateField(null=True)
    photo = models.FilePathField(path='BookList/static/img/', default='img/no_photo.png')

    def __str__(self):
        return self.username

class List(models.Model):
    user_id = models.ForeignKey(User, blank=False, default=1, unique=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mylists')
