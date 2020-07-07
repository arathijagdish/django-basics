from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from . models import User
from .forms import UserForm, CustomerForm

# Create your views here.
def register(request):
    if request.method == "GET":
        uf = UserForm()
        cf = CustomerForm()

        forms = {
            'userform': uf,
            'customerform': cf
        }
        return render(request, 'accounts/register.html', forms)
    else:
        uf = UserForm(request.POST)
        cf = CustomerForm(request.POST)
        if uf.is_valid() and cf.is_valid():
            password = uf.cleaned_data["password"]
            usr = uf.save(commit=False)
            usr.set_password(password)
            usr.save()

            customer = cf.save(commit=False)
            customer.user = usr
            customer.save()

            return HttpResponse('Data Saved')
        else:
            forms = {
                'userform': uf,
                'customerform': cf
            }
            return render(request, 'accounts/register.html', forms)

