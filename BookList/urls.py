from django.urls import path, include
from django.contrib.auth.views import LoginView
from BookList import views


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('account/signup/', views.SignUp.as_view(), name='signup'),
	path('account/login/', LoginView.as_view(), name = 'login'),
	path('', include('django.contrib.auth.urls')),
	path('account/logout/', views.logout, name = 'logout'),
	path('authors/', views.authors, name = 'authors'),
	path('mylists/', views.mylists, name = 'mylists'),
	path('mylists/create_list/', views.CreateList.as_view(), name='create_list'),
	path('account/', views.account, name = 'account')
]
