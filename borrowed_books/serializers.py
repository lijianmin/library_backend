from rest_framework import serializers
from borrowed_books.models import BorrowedBook
from books.models import Book
from django.contrib.auth.models import User

# Borrowed Book serializer
class BorrowedBookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    return_date = serializers.DateField()
    borrowed_since = serializers.DateTimeField(read_only=True)
    borrowed_by = serializers.ReadOnlyField(source='borrowed_by.user')
    borrowed = serializers.ReadOnlyField(source='book.borrowed')

    class Meta:
        model = BorrowedBook
        fields = ('id', 'book', 'return_date', 'borrowed_by','borrowed_since')

    def create(self, validated_data):
        """
        Create and return a new `BorrowedBook` instance, given the validated data.
        """
        return BorrowedBook.objects.create(**validated_data)