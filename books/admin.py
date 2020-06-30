from django.contrib import admin
from . models import Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser