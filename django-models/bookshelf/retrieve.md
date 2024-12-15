from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
print(my_book)
#expected output #1984 George Orwell 1949