from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from flask import redirect

from .models import Book
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