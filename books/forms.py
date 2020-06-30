from django.forms import ModelForm, TextInput, DateInput, Select
from . models import Book

class NewBookForm(ModelForm):

    class Meta():
        model = Book
        exclude = ('id',)
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Book Name"
                }
            ),
            'publisher': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Publisher Name"
                }
            ),
            'isbn': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "ISBN"
                }
            ),
            'publish_date': DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'author': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }