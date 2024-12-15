from bookshelf.models import Book
Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
#bk = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
#bk.save()
#No Error Message displayed.
#<Book: 1984 George Orwell 1949>
