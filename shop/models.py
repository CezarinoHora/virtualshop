from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
        ]
        verbose_name='categoria'
        verbose_name_plural='categorias'
