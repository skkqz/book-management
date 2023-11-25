from django.db import models


class Book(models.Model):
    """
    Модель книги
    """

    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=50, verbose_name='Автор книги')
    year = models.DateField(verbose_name='Дата издания')
    isbn = models.CharField(max_length=13, verbose_name='isbn код')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
