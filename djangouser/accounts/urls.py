from django.urls import path
from . import views as v

urlpatterns = [
    # path('login/', v.login, name="user_login"),
    path('register/', v.register, name="user_registration"),

]