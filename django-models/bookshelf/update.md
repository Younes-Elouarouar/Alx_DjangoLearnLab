from bookshelf.models import Book
my_book = Book.objects.get(id = 1)
my_book.title = 'Nineteen Eighty-Four'
my_book.save()
#expected output #Nineteen Eighty-Four George Orwell 1949