from django.shortcuts import render
from .forms import CourseForm

# Create your views here.
def new_course(request):
    if request.method == "GET":
        return render(request, 'course/newcourse.html', {'form': CourseForm()})