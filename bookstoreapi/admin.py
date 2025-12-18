from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')
    list_filter = ('author',)
    search_fields = ('title',)
