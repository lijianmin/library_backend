# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('books', request=request, format=format),
        'users': reverse('users', request=request, format=format),
        #'book reviews': reverse('book_reviews', request=request, format=format),
        #'user reviews': reverse('user_reviews', request=request, format=format),
        'borrowed books (or borrow a new book)': reverse('list_borrowedbook', request=request, format=format),
        'your reviews of users': reverse('users_review_byuser', request=request, format=format),
        'your reviews of books': reverse('books_review_byuser', request=request, format=format),
    })