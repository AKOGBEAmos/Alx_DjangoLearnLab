from django.db import models

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