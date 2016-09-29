from rest_framework import serializers
from reviews.models import book_review, user_review, RATING_CHOICES
from books.models import Book
from django.contrib.auth.models import User

# Book Review serializer
class BookReviewSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    for_book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    review_desc = serializers.CharField(required=True, allow_blank=False, max_length=10000)
    reviewed_by = serializers.ReadOnlyField(source='owner.username')
    rating = serializers.ChoiceField(choices=RATING_CHOICES, default=1)

    class Meta:
        model = book_review
        fields = ('id', 'for_book', 'review_desc', 'rating')

    def create(self, validated_data):
        """
        Create and return a new `book_review` instance, given the validated data.
        """
        return book_review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `book_review` instance, given the validated data.
        """
        instance.review_desc = validated_data.get('review_desc', instance.review_desc)
        instance.save()
        return instance

# User Review serializer
class UserReviewSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    for_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    review_desc = serializers.CharField(required=True, allow_blank=False, max_length=10000)
    reviewed_by = serializers.ReadOnlyField(source='owner.username')
    rating = serializers.ChoiceField(choices=RATING_CHOICES, default=1)

    class Meta:
        model = user_review
        fields = ('id', 'for_user', 'review_desc', 'rating')

    def create(self, validated_data):
        """
        Create and return a new `book_review` instance, given the validated data.
        """
        return user_review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `book_review` instance, given the validated data.
        """
        instance.review_desc = validated_data.get('review_desc', instance.review_desc)
        instance.save()
        return instance