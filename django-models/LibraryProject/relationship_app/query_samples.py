import os
import sys
import django

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_samples():
    # Filter books by Author
    def get_books_by_author(author_name):
        try:
            author = Author.objects.get(name=author_name)
            return Book.objects.filter(author=author)
        except Author.DoesNotExist:
            return None

    # List all books in a library 
    def get_library_books(library_name):
        try:
            library = Library.objects.get(name=library_name)
            return library.books.all()
        except Library.DoesNotExist:
            return None

    # Get librarian from a library
    def get_library_librarian(library_name):
        try:
            return Librarian.objects.get(library=Library.objects.get(name=library_name))
        except (Library.DoesNotExist, Librarian.DoesNotExist):
            return None
        



    # Sample data
    author = Author.objects.create(name="J.K. Rowling")
    book = Book.objects.create(title="Harry Potter", author=author)
    library = Library.objects.create(name="City Library")
    library.books.add(book)
    librarian = Librarian.objects.create(name="John Smith", library=library)

    print("\nBooks by J.K. Rowling:")
    books = get_books_by_author("J.K. Rowling")
    for book in books:
        print(f"- {book.title}")

    print("\nBooks in City Library:")
    books = get_library_books("City Library")
    for book in books:
        print(f"- {book.title}")

    print("\nLibrarian at City Library:")
    librarian = get_library_librarian("City Library")
    if librarian:
        print(f"- {librarian.name}")

if __name__ == "__main__":
    query_samples()