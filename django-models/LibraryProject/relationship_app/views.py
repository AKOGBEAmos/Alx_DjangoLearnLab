from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    book_list = {book_list: books}
    return render(request, 'relationship_app/list_books.html', book_list)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        # Add books to the context
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  
        return context
