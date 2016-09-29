from django.http                    import Http404
from rest_framework.views           import APIView
from rest_framework.response        import Response
from rest_framework                 import status
from rest_framework                 import generics
from rest_framework                 import permissions

from books.models					import Book
from books.serializers              import BookSerializer, UserSerializer
from books.permissions              import IsOwnerOrReadOnly

from django.contrib.auth.models     import User

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookList(APIView):
    
    """
    List all books or create a new book
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # RETRIEVE all books - entire paginated list or per user (/?userid=id)
    def get(self, request, format=None):
        
        if not request.GET.get('userid'):
            books = Book.objects.all()
        else:
            books = Book.objects.filter(owner=request.GET.get('userid'))

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # CREATE a new book per user - user must be authenticated
    def post(self, request, format=None):
        
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    
    """
    Retrieve details of a book
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class ManageBook(APIView):
    
    """
    Update or delete a Book - User must be authenticated 
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            book = Book.objects.get(pk=pk)
            return book
        except Book.DoesNotExist:
            raise Http404

    # UPDATE a book - User must be authenticated and also the owner of the book
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        
        if book.owner.id == self.request.user.id:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"Not Authorized":"You are not the owner of this book"}, status=status.HTTP_403_FORBIDDEN)

    # DELETE a book - User must be authenticated and also the owner of the book
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        
        if book.owner.id == self.request.user.id:
            book.delete()
            return Response({"Success":"Book deleted"}, status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({"Not Authorized":"You are not the owner of this book"}, status=status.HTTP_403_FORBIDDEN)