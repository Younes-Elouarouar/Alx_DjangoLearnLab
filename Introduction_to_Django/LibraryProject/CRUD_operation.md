# Import the model
from bookshelf.models import Book

# Create a new book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # This should work without error

# Retrieve and print all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)  # Should show <QuerySet []>
