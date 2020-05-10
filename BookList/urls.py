from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from BookList import views
from BookList.models import List


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('account/signup/', views.SignUp.as_view(), name='signup'),
	path('account/login/', LoginView.as_view(), name = 'login'),
	path('', include('django.contrib.auth.urls')),
	path('account/logout/', views.logout, name = 'logout'),
	path('authors/', views.authors, name = 'authors'),
	path('mylists/', views.mylists, name = 'mylists'),
	path('mylists/create_list/', views.CreateList.as_view(), name='create_list'),
	path('account/', views.account, name = 'account'),
	path('lists/<int:pk>', DetailView.as_view(model=List, template_name='mylists/list_detail.html'), name='list_detail'),
	path('books/', views.books, name = 'books'),
	path('books/create_book/', views.CreateBook.as_view(), name = 'create_book'),
	path('books/update_book/<str:pk>/', views.update_book, name = 'update_book'),
	path('books/delete_book/<str:pk>/', views.delete_book, name = 'delete_book')
]
