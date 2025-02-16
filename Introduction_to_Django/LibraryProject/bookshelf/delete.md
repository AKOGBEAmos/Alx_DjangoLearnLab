# Delete a Book Instance

This command deletes the book previously created and confirms the deletion by attempting to retrieve all books.

```python
# Python command to delete the book and confirm deletion
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(f"Remaining books: {list(books)}")

# Expected output: Confirms the deletion by showing an empty list of books
# Remaining books: []