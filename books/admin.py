from django.db import models
from django.urls import reverse

from genres.models import Genre
from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")
    genre = models.ForeignKey(Genre, null=True, related_name="catalog", on_delete=models.SET_NULL, blank=True,
                              verbose_name="Жанр книги")
    author = models.ForeignKey(Author, null=True, related_name="catalog", on_delete=models.SET_NULL, blank=True,
                               verbose_name="Имя автора")

    #    def get_absolute_url(self):
    #        return reverse('details', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('author', 'name')
        unique_together = ('name', 'author', 'genre')
