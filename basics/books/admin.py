from django.contrib import admin
from . models import Book, Author, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser