from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.new_course, name="new_course"),
]