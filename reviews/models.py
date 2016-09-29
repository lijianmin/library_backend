from django.db import models
from books.models import Book
from django.contrib.auth.models import User

RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

# Create your models here.
class book_review(models.Model):
    for_book = models.ForeignKey(Book, related_name='book_review')
    review_desc = models.CharField(max_length=10000)
    reviewed_on = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(User, related_name='book_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

class user_review(models.Model):
    for_user = models.ForeignKey(User, related_name='book_review')
    review_desc = models.CharField(max_length=10000)
    reviewed_on = models.DateTimeField(auto_now_add=True)
    reviewed_by = models.ForeignKey(User, related_name='user_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
