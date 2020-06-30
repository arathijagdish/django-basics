from django.shortcuts import render, HttpResponse, redirect
from .forms import NewBookForm
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all() # select * from books
    return render(request, 'books/home.html', {'data': books})

# Create your views here.
def new_book(request):
    if request.method == "GET":
        nbf = NewBookForm()
        return render(request, 'books/newbook.html', {'form': nbf})
    else:
        nbf = NewBookForm(request.POST)
        if nbf.is_valid():
           nbf.save()
           return redirect('book_home')
        else:
            return render(request, 'books/newbook.html', {'form': nbf})

def delete_book(request, id):
    if id > 0:
        Book.objects.get(pk=id).delete()
        return redirect('book_home')
    else:
        return HttpResponse(status=404)

def search_book(request):
    # if s == None:
    #     redirect('book_home')
    txt = request.GET.get('s')
    request.session["search"] = txt
    if txt == None:
        return redirect('book_home')
    books = Book.objects.filter(name__contains=txt)
    return render(request, 'books/search.html', {'data': books})


def edit_book(request, id):
    # Fetch the book object
    book = Book.objects.get(pk=id)
    if request.method == "GET":
        # Populate the form with data
        nbf = NewBookForm(instance=book)
        return render(request, 'books/editbook.html', {'form': nbf})
    else: # If method is POST
        nbf = NewBookForm(data=request.POST, instance=book)
        if nbf.is_valid():
            nbf.save()
            return redirect('book_home')
