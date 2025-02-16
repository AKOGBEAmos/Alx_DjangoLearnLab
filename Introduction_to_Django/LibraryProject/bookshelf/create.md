# Creating a Book Instance

This command creates a new Book instance in the database with the specified attributes.

```python
# Python command to create a Book instance
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output: 
# <Book: 1984 by George Orwell>