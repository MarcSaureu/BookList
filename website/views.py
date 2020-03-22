from django.shortcuts import render

def boby(request):
	return render(request, 'body.html', {})