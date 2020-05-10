from django.shortcuts import render
from flask import request

from django.contrib import auth
from django.views import generic
from django.urls import reverse_lazy
from BookList.forms import UserCreationForm, ListCreationForm
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
	return render(request, 'mylists.html', {})

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
