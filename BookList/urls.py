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
	path('books/update_book/<int:pk>/', views.update_book, name = 'update_book'),
	path('books/delete_book/<int:pk>/', views.delete_book, name = 'delete_book'),
	path('mylists/update_list/<int:pk>/', views.update_list, name = 'update_list'),
	path('mylists/delete:list/<int:pk>/', views.delete_list, name = 'delete_list'),
	path('authors/author/', views.CreateAuthor.as_view(), name = 'create_author'),
	path('authors/update_author/<str:pk>/', views.update_author, name = 'update_author'),
	path('authors/delete_author/<str:pk>/', views.delete_author, name = 'delete_author')
]
