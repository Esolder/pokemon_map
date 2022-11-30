from datetime import datetime

from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    img = models.ImageField('Изображение', null=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')
