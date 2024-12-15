from bookshelf.models import Book
bk = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
bk.save()
#No Error Message displayed.

from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
print(my_book)
#expected output #1984 George Orwell 1949

from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
my_book.title = 'Nineteen Eighty-Four'
my_book.save()
#expected output #Nineteen Eighty-Four George Orwell 1949

from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
my_book.delete()
#expected output #(1, {'bookshelf.Book': 1})