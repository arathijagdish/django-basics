from django.forms import ModelForm, TextInput, PasswordInput
from . models import User

class LoginForm(ModelForm):
    class Meta():
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': PasswordInput()
        }