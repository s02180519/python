from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="Автор")

    #    def get_absolute_url(self):
    #        return reverse('details', kwargs={'id': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ('name', )
