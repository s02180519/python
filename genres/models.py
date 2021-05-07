from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=32, verbose_name="Жанр")

    #    def get_absolute_url(self):
    #        return reverse('details', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('name',)
# Create your models here.
