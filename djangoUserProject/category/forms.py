from django import forms
from django.forms import TextInput, Select

from . models import Category, SubCategory

class CategoryForm(forms.ModelForm):
    """Form definition for NewCategory."""

    class Meta:
        """Meta definition for NewCategoryform."""

        model = Category
        fields = '__all__'

class SubCategoryForm(forms.ModelForm):
    """Form definition for NewCategory."""

    class Meta:
        """Meta definition for NewCategoryform."""

        model = SubCategory
        fields = '__all__'
