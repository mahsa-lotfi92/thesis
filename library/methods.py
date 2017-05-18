from datetime import datetime, timedelta

from library.models import Book
from ajax_testing.decorators import save_request


@save_request
def add_new_book(publish_date, price, name, desc, available, author):
    date = datetime.strptime(publish_date, "%Y/%m/%d")
    Book.objects.create(publish_date=date, price=price, name=name, description=desc, available=available, author=author)
    return True


@save_request
def get_books_by_date(start, end):
    start = datetime.strptime(start, "%Y/%m/%d") if start else datetime.today()+timedelta(days=-1)
    end = datetime.strptime(end, "%Y/%m/%d") if end else datetime.today()
    return Book.objects.filter(publish_date__gte=start, publish_date__lte=end).all()


@save_request
def get_books_by_name(name):
    books = []
    for b in Book.objects.all():
        if name in b.name:
            books.append(b)
    return books


@save_request
def get_available_books():
    books = []
    for b in Book.objects.all():
        if b.available > 0:
            books.append(b)
    return books


@save_request
def remove_book_by_id(id):
    Book.objects.get(id=id).delete()
    return True


@save_request
def buy_book_by_id(id):
    b = Book.objects.get(id=id)
    if b.available > 0:
        b.available -= 1
        b.save()
        return True
    else:
        return False