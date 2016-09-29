from django.http                    import Http404
from rest_framework.views           import APIView
from rest_framework.response        import Response
from rest_framework                 import status
from rest_framework                 import generics
from rest_framework                 import permissions

from reviews.models					import book_review, user_review
from reviews.serializers            import BookReviewSerializer, UserReviewSerializer

from django.contrib.auth.models     import User

from reviews.permissions            import IsOwnerOrReadOnly

# Create your views here.
# =========================== BOOK REVIEWS ===============================
class BookReviewList(APIView):

    """
    Retrieve all reviews of a book
    """
    
    # RETRIEVE all reviews of a book
    def get(self, request, book_id, format=None):

        reviews = book_review.objects.filter(for_book=book_id)
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookReviewDetails(APIView):
    
    """
    Retrieve a particular review of a book
    """

    # RETRIEVE a book review
    def get(self, request, pk, format=None):
        reviews = book_review.objects.get(pk=pk)
        serializer = BookReviewSerializer(reviews, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SubmitBookReview(APIView):

    """
    Submit a review of a particular book - User must be authenticated
    """ 

    permission_classes = (permissions.IsAuthenticated,)

    # CREATE a book review
    def post(self, request, format=None):
            
        serializer = BookReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(reviewed_by = self.request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"Error":"Unable to add book review", "Details":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ManageBookReview(APIView):
    
    """
    Update or delete a book review - User must be authenticated
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # UPDATE a book review
    def put(self, request, pk, format=None):
        review = book_review.objects.get(pk=pk)
        serializer = BookReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE a book review
    def delete(self, request, pk, format=None):
        review = book_review.objects.get(pk=pk)
        book.delete()
        return Response({"success":"book review deleted"}, status=status.HTTP_204_NO_CONTENT)

class BookReviewListByUser(APIView):
    
    """
    Retrieve all books reviews made by a user - User must be authenticated
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    # RETRIEVE all user's book reviews
    def get(self, request, format=None):
        
        reviews = book_review.objects.filter(reviewed_by=self.request.user.id)
        serializer = BookReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# =========================== USER REVIEWS ===============================
class UserReviewList(APIView):
    
    """
    Retrieve all reviews of a user
    """

    # RETRIEVE all reviews of a user - public viewing
    def get(self, request, user_id, format=None):
        
        reviews = user_review.objects.filter(for_user=user_id)
        serializer = UserReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserReviewDetails(APIView):

    """
    Retrieve a particular review of a user
    """

    # RETRIEVE a user review
    def get(self, request, pk, format=None):
        reviews = user_review.objects.get(pk=pk)
        serializer = UserReviewSerializer(reviews, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SubmitUserReview(APIView):
    
    """
    Submit a review of a particular user - User must be authenticated
    """

    permission_classes = (permissions.IsAuthenticated,)

    # CREATE a user review
    def post(self, request, format=None):
            
        serializer = UserReviewSerializer(data=request.data)
        
        # add a logic to make sure no ownself review ownself
        if serializer.is_valid():
            serializer.save(reviewed_by = self.request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"Error":"Unable to add user review", "Details":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class ManageUserReview(APIView):
    
    """
    Update or delete a user review - User must be authenticated
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    # UPDATE a user review
    def put(self, request, pk, format=None):
        review = user_review.objects.get(pk=pk)
        serializer = UserReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE a user review
    def delete(self, request, pk, format=None):
        review = user_review.objects.get(pk=pk)
        book.delete()
        return Response({"success":"user review deleted"}, status=status.HTTP_204_NO_CONTENT)   

class UserReviewListByUser(APIView):
    
    """
    Retrieve all users reviews made by a user - User must be authenticated
    """

    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    # RETRIEVE all user's user reviews
    def get(self, request, format=None):
        
        reviews = user_review.objects.filter(reviewed_by=self.request.user.id)
        serializer = UserReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    