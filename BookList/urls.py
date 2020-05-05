from django.urls import path, include
from django.contrib.auth.views import LoginView
from BookList import views


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('', include('django.contrib.auth.urls')),
	path('logout/', views.logout, name = 'logout'),
	path('mylists/', views.mylists, name = 'mylists'),
	path('authors/', views.authors, name = 'authors')
]
