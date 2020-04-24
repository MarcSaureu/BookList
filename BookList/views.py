from django.shortcuts import render
from django.contrib import auth
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

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
	template_name = 'sign_up.html'