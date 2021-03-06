"""lendbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls), # Django Admin
    url(r'^', include('books.urls')), # Books Management
    url(r'^', include('borrowed_books.urls')), # Borrow Books
    url(r'^', include('reviews.urls')), # Reviews
    url(r'^', include('api_root.urls')), 
    url(r'^api-token-auth/', obtain_jwt_token), # JWT
    url(r'^', include('django.contrib.auth.urls')), # Django's own Auth'
    url(r'^account/', include('rest_auth.urls')), # Account Management
    url(r'^account/registration/', include('rest_auth.registration.urls')), # Account Registration
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

