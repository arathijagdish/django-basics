from django.shortcuts import render, HttpResponse, redirect
from . forms import LoginForm
from . models import User

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html', {'form': LoginForm()})
    else:
        user = User.objects.filter(email = request.POST.get('email'), password = request.POST.get('password'))
        if len(user) == 1: # If user exists
            return redirect("https://www.bing.com")
        else:
            return render(request, 'user/login.html', {'form': LoginForm, 'message': 'Invalid user'})
