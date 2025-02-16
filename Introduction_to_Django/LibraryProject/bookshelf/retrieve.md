# Retrieve a Book Instance

This command retrieves and displays all attributes of the book previously created.

```python
# Python command to retrieve and display the book
from books.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

# Expected output: Displays the details of the book
# Title: 1984, Author: George Orwell, Publication Year: 1949