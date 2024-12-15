from bookshelf.models import Book
**Command**:
```python
book.objects.delete()
book.delete()

books = Book.objects.all()
print(books)  # Should return an empty queryset
