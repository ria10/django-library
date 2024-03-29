from django.shortcuts import redirect, render
from library.forms import NewBookForm
from library.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(req):
    return render(req, 'library/index.html')
@login_required    
def show(req):
    context = { 'books' : Book.objects.all() }
    return render(req, 'library/all-books.html',context)
@login_required
def showbyid(req,id):
    context = { 'books' : Book.objects.filter(id=id) }
    return render(req, 'library/book.html', context)
def new_book(req):
    if req.method == 'POST':
        form = NewBookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('books-show')
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(req, 'library/new-book.html', data)
