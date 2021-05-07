from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from books.views import create, show_books, details, main

urlpatterns = [
    path('create/', create, name='create'),
    path('show_books/', show_books, name='show_books'),
    path('details/', details, name='details'),
    path('main/', main, name='main')

]