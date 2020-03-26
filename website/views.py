from django.shortcuts import render
from django.contrib import auth
from .models import User

def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'forms/login.html', {})

def logout(request):
	auth.logout(request)
	return render(request, 'home.html', {})
