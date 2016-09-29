from django.db import models
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.
class BorrowedBook (models.Model):
    borrowed_by = models.ForeignKey(User, related_name='borrowed_books')
    book = models.OneToOneField(Book)
    borrowed_since = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()