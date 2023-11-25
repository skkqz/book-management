from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    """
    Представление списка книг
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Детально представление книги
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
