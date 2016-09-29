from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User

# Book serializer
class BookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    author = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    summary = serializers.CharField(required=True, allow_blank=False, max_length=500)
    owner = serializers.ReadOnlyField(source='owner.username')
    borrowed = serializers.BooleanField(required=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'summary', 'owner', 'borrowed')

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.borrowed = validated_data.get('borrowed', instance.borrowed)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')