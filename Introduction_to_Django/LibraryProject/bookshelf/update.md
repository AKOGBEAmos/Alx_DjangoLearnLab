# Update a Book Instance

This command updates the title of the book from "1984" to "Nineteen Eighty-Four" and saves the changes.

```python
# Python command to update the book's title
from books.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")

# Expected output: Displays the updated title of the book
# Updated Title: Nineteen Eighty-Four