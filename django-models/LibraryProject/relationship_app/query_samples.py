from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author.
author_name = "author_name"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book.title)
#List all books in a library.
library_name = "library_name"
library = Library.objects.get(name=library_name)
books = library.books.all()

#Retrieve the librarian for a library.
librarian_name = "librarian_name"
librarian = Librarian.objects.get(library=librarian_name)
library = librarian.library