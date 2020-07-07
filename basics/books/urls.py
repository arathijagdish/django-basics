from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home, name='book_home'),
    path('create/', v.new_book, name='book_create'),
    path('delete/<int:id>/', v.delete_book, name='book_delete'),
    path('search/', v.search_book, name='book_search'),
    path('edit/<int:id>', v.edit_book, name='book_edit'),
]