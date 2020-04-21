from django.urls import path
from django.contrib.auth.views import LoginView
from BookList import views
from BookList.views import RegistroUsuario


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('registro/',RegistroUsuario.as_view(), name = 'sign')
]
