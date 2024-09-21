from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.

from django.shortcuts import render, redirect
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_added')  # Redirect after successful form submission
    else:
        form = BookForm()

    return render(request, 'book/book_templates.html', {'form': form})

def success(request):

    return HttpResponse("Book was succefully added")

def show_book_content(request):
    show_content = Book.objects.all()
    books_list = []
    
    for book in show_content:
        books_list.append(book)


    

    return HttpResponse(books_list)