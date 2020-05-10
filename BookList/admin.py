from django.contrib import admin
from .models import User, Author, Book, List
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from BookList import models, forms

# Register your models here.

class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	add_form = forms.UserCreationForm
	form = forms.UserChangeForm

	# The custom user model we are going to use
	model = models.User

	fieldsets = BaseUserAdmin.fieldsets + (
       	('Personal info', {'fields': ('birth_date', 'photo',)}),
	)

admin.site.register(models.User, UserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(List)
