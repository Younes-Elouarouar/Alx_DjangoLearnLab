from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
my_book.delete()
#expected output #(1, {'bookshelf.Book': 1})