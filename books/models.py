from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    """
    Модель книги
    """

    grate_list = [
        (1, '1 🌟'),
        (2, '2 🌟'),
        (3, '3 🌟'),
        (4, '4 🌟'),
        (5, '5 🌟'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=50, verbose_name='Автор книги')
    year = models.DateField(verbose_name='Дата издания')
    isbn = models.IntegerField(max_length=13, verbose_name='isbn код')
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], choices=grate_list,
                                 blank=True, null=True, verbose_name='рейтинг')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
