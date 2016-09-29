from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200)
    added_since = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    summary = models.CharField(max_length=500)
    owner = models.ForeignKey(User, null=True, related_name='books')
    borrowed = models.BooleanField(default=False)

