from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    url(r'^books/$', views.BookList.as_view(), name='books'),
    url(r'^book/view/(?P<pk>[0-9]+)/$', views.BookDetails.as_view(), name='book_details'),
    url(r'^book/manage/(?P<pk>[0-9]+)/$', views.ManageBook.as_view(), name='manage_book'),
    url(r'^users/$', views.UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)