from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=4)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Book: {self.title} by {self.author} in {self.publication_year}"

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
    
class UserProfile(User):
    role =  models.CharField(max_length=40)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")

    USERNAME_FIELD = "email"

    # Signal to create UserProfile when a User is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    # Function to save UserProfile when the User is updated
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    # Connect signals directly without using @receiver
    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User)