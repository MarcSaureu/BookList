from django.urls import path
from django.contrib.auth.views import LoginView
from BookList import views


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('logout/', views.logout, name = 'logout')
]
