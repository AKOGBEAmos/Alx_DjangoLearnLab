from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "{self.name}"

class Book(models.Model):
    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    title = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=4)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Book: {self.title} by {self.author} in {self.publication_year}"

    #Adding a new book
    def add_book(title,author):
        book = Book.objects.create(title= title, author=author)

#Form to manage the book objects
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','publication_year']


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    
    def list_book(self):
        for book in self.books:
            print(book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=40, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    # Signal to create UserProfile when a User is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            # Crée le profil seulement s'il n'existe pas déjà
            UserProfile.objects.get_or_create(user=instance, defaults={'role': 'Member'})

    # Function to save UserProfile when the User is updated
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    # Connect signals directly without using @receiver
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)