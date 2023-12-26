from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        else:
            print(add_book.errors)
    
        add_caregory = CategoryForm(request.POST)
        if add_caregory.is_valid():
            add_caregory.save()

    context = {
        'category': Category.objects.all(),
        'book': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm()

    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'category': Category.objects.all(),
        'book': Book.objects.all(),
        'formcat': CategoryForm()
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id = id)     # get id  = the id of the object (book)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance = book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')

    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form' : book_save,
    }

    return render(request, 'pages/update.html', context)

def delete(request, id):

    book_delete = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_delete.delete()
        return redirect('/')

    return render(request, 'pages/delete.html')


