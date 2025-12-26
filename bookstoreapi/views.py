from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    filterset_fileds = ['author', 'stock']
    search_fields = ['title', 'author__name']
    ordering_fields = ['created_at', 'title', 'price']
    ordering = ['-created_at']

