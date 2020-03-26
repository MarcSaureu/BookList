from django.urls import path
from django.contrib.auth.views import LoginView
from website import views


urlpatterns = [
	path('', views.home, name = 'website'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('logout/', views.logout, name = 'logout')
]