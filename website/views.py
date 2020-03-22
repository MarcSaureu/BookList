from django.shortcuts import render

def boby(request):
	render(request, 'login_header.html', {})
	return render(request, 'body.html', {})