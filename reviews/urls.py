from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from reviews import views

urlpatterns = [
    url(r'^reviews/book/$', views.SubmitBookReview.as_view(), name='submit_book_review'),
    url(r'^reviews/book/all/(?P<book_id>[0-9]+)/$', views.BookReviewList.as_view(), name='book_reviews_list'),
    url(r'^reviews/book/detail/(?P<pk>[0-9]+)/$', views.BookReviewDetails.as_view(), name='book_review_details'),
    url(r'^reviews/book/manage/(?P<pk>[0-9]+)/$', views.ManageBookReview.as_view(), name='manage_book_review'),
    url(r'^reviews/allbooks/$', views.BookReviewListByUser.as_view(), name='all_book_review_by_user'),

    url(r'^reviews/user/$', views.SubmitUserReview.as_view(), name='submit_user_review'), 
    url(r'^reviews/user/all/(?P<user_id>[0-9]+)/$', views.UserReviewList.as_view(), name='user_reviews_list'),
    url(r'^reviews/user/detail/(?P<pk>[0-9]+)/$', views.UserReviewDetails.as_view(), name='user_review_details'),
    url(r'^reviews/user/manage/(?P<pk>[0-9]+)/$', views.ManageUserReview.as_view(), name='manage_user_review'),
    url(r'^reviews/allusers/$', views.UserReviewListByUser.as_view(), name='all_user_review_by_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)