from django.http                    import Http404
from rest_framework.views           import APIView
from rest_framework.response        import Response
from rest_framework                 import status
from rest_framework                 import generics
from rest_framework                 import permissions

from books.models					import Book
from borrowed_books.models          import BorrowedBook
from borrowed_books.serializers     import BorrowedBookSerializer
from books.permissions              import IsOwnerOrReadOnly

from django.contrib.auth.models     import User

from rest_framework                 import generics

# Create your views here.
class BorrowedBookList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    # get all borrowed books belonging to the user - DONE
    def get(self, request, format=None):
        
        borrowed_books = BorrowedBook.objects.filter(borrowed_by = self.request.user.id)
        serializer = BorrowedBookSerializer(borrowed_books, many=True)
        return Response(serializer.data)

    # "borrow" a book by adding it to borrowed list then mark the book as borrowed
    def post(self, request, format=None):
        
        _book = Book.objects.get(pk=request.data['book'])

        if(_book.borrowed != True) :
            
            serializer = BorrowedBookSerializer(data=request.data)
        
            if serializer.is_valid():
                serializer.save(borrowed_by=self.request.user)

                # Mark book borrowed as true - book borrowed
                _book.borrowed = True
                _book.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:        
            return Response({"Error":"Book has been borrowed"}, status=status.HTTP_400_BAD_REQUEST)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Manage Books - either view all or "borrow" a book 
class BorrowedBookDetails(APIView):
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

    # get details of borrowed book from the user
    def get(self, request, pk, format=None):
        
        borrowed_book = BorrowedBook.objects.filter(borrowed_by = self.request.user.id).get(pk=pk)
        serializer = BorrowedBookSerializer(borrowed_book, many=False)
        return Response(serializer.data)

    # return book (also means delete book from borrowed book list) and un-borrow the book
    def delete(self, request, pk, format=None):
        
        borrowed_book = BorrowedBook.objects.get(pk=pk)
        
        # mark book borrowed as false - book returned
        borrowed_book_id = borrowed_book.book_id
        _book = Book.objects.get(pk=borrowed_book_id)
        _book.borrowed = False
        _book.save()

        #remove borrowed_book from list
        borrowed_book.delete()

        return Response({"Success":"Book has been returned"}, status=status.HTTP_200_OK)

        
    
