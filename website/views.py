from django.shortcuts import render
from .models import User

def home(request):
	users = User.objects.all()
	
	context = {
		'users' : users
	}

	return render(request, 'home.html', context)

"""
from website.models import User                                                         

u1 = User( 
	first_name='Daniel', 
	last_name='Farré Serra', 
	birth_date='1997-10-09', 
	user_alias='Dani', 
	email='danifarre97@gmail.com', 
	password='user' 
	)                                                                                       

u1.save() 
"""