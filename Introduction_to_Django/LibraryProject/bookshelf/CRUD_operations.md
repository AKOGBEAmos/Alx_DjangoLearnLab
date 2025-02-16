## CRUD Operations

The four operations that we performed on the Book app are here with detailed description.

# Creation of new book
```python
# Python command to create a Book instance
from books.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book) 

```

# Retrieving a specific book

```python
# Python command to retrieve and display the book
from books.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
```

# Updating the title of a book

```python
# Python command to update the book's title
from books.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")
```

# Deleting a book

```python
# Python command to delete the book and confirm deletion
from books.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(f"Remaining books: {list(books)}")