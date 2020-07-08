from django import forms
from django.forms import (
    Form,
    CharField,
    URLField,
    Select,
    TextInput,
    URLInput
)

class CourseForm(Form):
    title=CharField(
        label='Title',
        strip=True,
        min_length=5,
        help_text='Please pick a unique title',
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    video_link=URLField(
        label='Video URL',
        min_length=5,
        help_text='Please provide the video url',
        widget=URLInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    category=CharField(
        label='Category',
        min_length=3,
        widget=Select(
            attrs={
                'class': 'form-control',
                'id': 'category',
            },
        )
    )
    subcategory=CharField(
        label='Sub Category',
        min_length=5,
        widget=Select(
            attrs={
                'class': 'form-control',
                'id': 'subcategory',
            }
        )
    )
