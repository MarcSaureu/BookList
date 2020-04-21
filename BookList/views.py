from django.shortcuts import render
from django.contrib import auth
from .models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'forms/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'home.html', {})

class RegistroUsuario(CreateView):
	model = User
	template_name = "registration/sign_up.html"
	form_class = UserCreationForm
	success_url = reverse_lazy('BookList')
