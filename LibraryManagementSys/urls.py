"""LibraryManagementSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookslib import views
from rest_framework import routers
from bookslib import apiviews

router = routers.DefaultRouter()
router.register('books', apiviews.BooksApi, basename='books')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.admin_login, name='admin_login'),
    path('books_api', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('adminregister', views.admin_register, name='admin_register'),
    path('adminhome', views.admin_home, name='admin_home'),
    path('adminlogout', views.admin_logout, name='admin_logout'),
    path('addbook', views.add_book, name='add_book'),
    path('updatebook<int:pk>', views.update_book, name='update_book'),
    path('bookdetail<int:pk>', views.book_detail, name='book_detail'),
    path('deletebook<int:pk>', views.delete_book, name='delete_book'),
]
