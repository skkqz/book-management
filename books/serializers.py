from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Сериализер модели книги
    """

    class Meta:
        model = Book
        fields = '__all__'
