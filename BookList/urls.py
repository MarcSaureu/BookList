from django.urls import path, include
from django.contrib.auth.views import LoginView
from BookList import views


urlpatterns = [
	path('', views.home, name = 'BookList'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('', include('django.contrib.auth.urls')),
	path('logout/', views.logout, name = 'logout'),
	path('books/', views.books, name = 'books'),
	path('authors/', views.authors, name = 'authors'),
	path('lists/', views.lists, name = 'lists'),
	path('books/create_book', views.CreateBook.as_view(), name = 'create_book'),
	path('books/update_book', views.update_book, name = 'update_book'),
	path('books/delete_book' , views.delete_book, name = 'delete_book')
]
