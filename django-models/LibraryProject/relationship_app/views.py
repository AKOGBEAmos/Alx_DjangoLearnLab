from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, permission_required
from flask import redirect

from .models import Book, BookForm
from .models import Library
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def list_books(request):
    books = Book.objects.all()
    book_list = {'books': books}
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

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

def register(request):
    if request.method == 'POST':
        form_class = UserCreationForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login view
    else:
        form_class = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form_class})

@login_required
def profile(request):
    return render(request, 'relationship_app/profile.html') 

# Check if user is an admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Check if user is a librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Check if user is a member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

#Add new book 
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Crée le livre avec les données du formulaire
            form.save()
            return redirect('book_list')  # Redirige vers la liste des livres après l'ajout
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

#Modifying a book
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_title, new_title):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
        
        form = BookForm()
    return render(request, 'relationship_app/edit_book.html', {'form': form})

    """ book_id = Book.objects.get(title=book_title)
    book = Book.objects.get(id=book_id)
    book = Book.objects.get(title=book_title)
    book.title = new_title
    book.save()
    return HttpResponse(f"Book '{new_title}' updated!") """

#Deleting a book
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_title):
    book_id = Book.objects.get(title=book_title)
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponse(f"Book '{book.title}' deleted!")