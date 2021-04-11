from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    print("*"*100)
    print("This is the index rendering")
    context = {
        'books' : Book.objects.all()
    }
    return render(request, "books_app/index.html", context)

def add_book(request):
    print("*"*100)
    print("processing new book")
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def book_info(request, book_id):
    print('*'*100)
    print("this is the book info page")
    context = {
        'books' : Book.objects.get(id = book_id),
        'authors' : Book.objects.get(id = book_id).authors.all(),
        'all_authors' : Author.objects.all(),
    }
    return render(request, "books_app/book_info.html", context)

def append_authors(request, book_id):
    option = Author.objects.get(id = request.POST['select_author'])
    Book.objects.get(id = book_id).authors.add(option)
    return redirect(f'/book_info/{book_id}')



def authors(request):
    print("*"*100)
    print("This is the authors rendering")
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, "books_app/authors.html", context)

def add_author(request):
    print("*"*100)
    print("processing new author")
    new_author = Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('/authors')


def author_info(request, author_id):
    print('*'*100)
    print("this is the author info page")
    context = {
        'authors' : Author.objects.get(id = author_id),
        'books' : Author.objects.get(id = author_id).books.all(),
        'all_books' : Book.objects.all(),
    }
    return render(request, "books_app/author_info.html", context)


def append_books(request, author_id):
    option = Book.objects.get(id = request.POST['select_book'])
    Author.objects.get(id = author_id).books.add(option)
    return redirect(f'/author_info/{author_id}')