from django.shortcuts import render, render_to_response

from library.methods import *
from ajax_testing.decorators import save_request
from library.models import Book


@save_request
def add_book(request):
    publish_date = request.GET['date']
    price = request.GET['price']
    name = request.GET['name']
    desc = request.GET['desc']
    available = request.GET['available']
    author = request.GET['author']

    add_new_book(publish_date, price, name, desc, available, author)
    books = Book.objects.all()
    return render(request, 'book_store_management.html', {'books': books})



@save_request
def filter_by_date(request):
    start = request.GET['start']
    end = request.GET['end']
    books = get_books_by_date(start, end)
    return render_to_response('book_store.html', {'books': books})


@save_request
def filter_by_name(request):
    name = request.GET['name']
    books = get_books_by_name(name)
    return render_to_response('book_store.html', {'books': books})


def remove_book(request, id):
    remove_book_by_id(id)
    return render(request, 'book_store_management.html', {'books': Book.objects.all()})


def buy_book(request, id):
    buy_book_by_id(id)
    return render(request, 'book_store.html', {'books': Book.objects.all()})

def book_store(request):
    books = get_available_books()
    return render(request, 'book_store.html', {'books':books})


def book_store_management(request):
    books = Book.objects.all()
    return render(request, 'book_store_management.html', {'books':books})