from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from borrowed_books import views

urlpatterns = [
    url(r'^borrowedbooks/$', views.BorrowedBookList.as_view(), name='list_borrowedbook'),
    url(r'^borrowedbooks/(?P<pk>[0-9]+)/$', views.BorrowedBookDetails.as_view(), name='details_borrowedbook'),
]

urlpatterns = format_suffix_patterns(urlpatterns)