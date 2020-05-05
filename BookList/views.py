from django.shortcuts import render
from django.contrib import auth
from django.views import generic
from django.urls import reverse_lazy
from BookList.forms import UserCreationForm
from BookList.models import Book, Author


def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'forms/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'home.html', {})

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/sign_up.html'

def mylists(request):

	books = Book.objects.all()

	context = { 'books': books }
	return render(request, 'mylists.html', context)

def books(request):
	books = Book.objects.all()

	context = { 'books': books }
	return render(request, 'books.html', context)

def authors(request):
	authors = Author.objects.all()

	context = { 'authors': authors }
	return render(request, 'authors.html', context)	

