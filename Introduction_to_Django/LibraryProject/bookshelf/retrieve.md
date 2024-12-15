## Retrieve Operation

**Command**:
```python
books = Book.objects.all()
Book.objects.get()
for b in books:
    print(b.title, b.author, "1984")
