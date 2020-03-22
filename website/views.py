from django.shortcuts import render

def home(request):
	print('ok')
	return render(request, 'home.html', {})