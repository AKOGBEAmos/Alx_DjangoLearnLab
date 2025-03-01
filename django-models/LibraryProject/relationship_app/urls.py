from django.urls import path, include
from .views import list_books, LibraryDetailView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),

]