from django.contrib import admin
from author.models import Author


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', )


admin.site.register(Author, AuthorAdmin)
