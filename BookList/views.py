from django.shortcuts import render
from django.contrib import auth
from django.views import generic
from django.urls import reverse_lazy
from BookList.forms import UserCreationForm, BookCreationForm
from BookList.models import Book, Author, List


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

def lists(request):
	lists = List.objects.all()

	context = { 'lists' : lists}
	return render(request, 'lists.html', context)

def books(request):
	books = Book.objects.all()

	context = { 'books': books }
	return render(request, 'books.html', context)

def authors(request):
	authors = Author.objects.all()

	context = { 'authors': authors }
	return render(request, 'authors.html', context)

class CreateBook(generic.CreateView):
	model = Book
	template_name = 'form.html'
	form_class = BookCreationForm

def update_book(request, pk):
	book = Book.objects.get(ISBN=pk)
	form = BookCreationForm(instance=book)

	if request.method == 'POST':
		form= BookCreationForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('/books')
	context = {'form':form}
	return render(request, 'update_book.html', context)


def delete_book(request, pk):
	book = Book.objects.get(ISBN=pk)

	if request.method == 'POST':
		book.delete()
		return redirect('/books')

	context = {'item': book}
	return render(request, 'delete_book.html', context)
