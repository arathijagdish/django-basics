from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, CharField
from .models import User, Customer

class UserForm(ModelForm):
    """Form definition for User."""
    password1 = CharField(
        label="Confirm Password",
        widget=PasswordInput()
    )
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('email', 'password')

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('user',)
