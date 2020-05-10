from django.shortcuts import render, redirect
from flask import request

from django.contrib import auth
from django.views import generic
from django.urls import reverse_lazy
from BookList.forms import UserCreationForm, ListCreationForm, BookCreationForm, AuthorCreationForm
from django.views.generic.detail import DetailView
from BookList.models import Book, Author, List, User


def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'registration/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'home.html', {})

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

def mylists(request):
	lists = List.objects.all()

	context = { 'lists' : lists}
	return render(request, 'mylists.html', context)

def books(request):
	books = Book.objects.all()

	context = { 'books': books }
	return render(request, 'books.html', context)

def authors(request):
	authors = Author.objects.all()

	context = { 'authors': authors }
	return render(request, 'authors.html', context)

def account(request):
	return render(request, 'account.html', {})

class CreateList(generic.CreateView):
    model = List
    template_name = 'form.html'
    form_class = ListCreationForm

    def form_valid(self, form):
        form.user = self.request.user
        return super(CreateList, self).form_valid(form)

class RestaurantDetail(DetailView):
    model = List
    template_name = 'mylists/list_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ListDetail, self).get_context_data(**kwargs)
        return context

class CreateBook(generic.CreateView):
	model = Book
	template_name = 'form.html'
	form_class = BookCreationForm

def update_book(request, pk):
	book = Book.objects.get(ISBN=pk)
	form = BookCreationForm(instance=book)

	if request.method == 'POST':
		form = BookCreationForm(request.POST, instance=book)
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

def update_list(request, pk):
	list = List.objects.get(pk=pk)
	form = ListCreationForm(instance=list)

	if request.method == 'POST':
		form = ListCreationForm(request.POST, instance=list)
		if form.is_valid():
			form.save()
			return redirect('/mylists')

	context = {'form' : form}
	return render(request, 'update_list.html', context)

def delete_list(request, pk):
	list = List.objects.get(pk=pk)

	if request.method == 'POST':
		list.delete()
		return redirect('/mylists')

	context = {'item' : list}
	return render(request, 'delete_list.html', context)

class CreateAuthor(generic.CreateView):
	model = Author
	template_name = 'form.html'
	form_class = AuthorCreationForm

def update_author(request, pk):
	author = Author.objects.get(first_name=pk)
	form = AuthorCreationForm(instance=author)

	if request.method == 'POST':
		form = AuthorCreationForm(request.POST, instance=author)
		if form.is_valid():
			form.save()
			return redirect('/authors')

	context = {'form' : form}
	return render(request, 'update_author.html', context)

def delete_author(request, pk):
	author = Author.objects.get(first_name=pk)

	if request.method == 'POST':
		author.delete()
		return redirect('/authors')

	context = {'item' : author}
	return render(request, 'delete_author.html', context)
