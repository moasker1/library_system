from django.shortcuts import render
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

def delete(request):
    return render(request, 'pages/delete.html')

def update(request):
    return render(request, 'pages/update.html')

