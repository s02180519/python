from django.contrib import admin
from books.models import Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'name')
    list_display = ('author', 'name', 'genre')


admin.site.register(Book, BookAdmin)
