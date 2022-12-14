from datetime import datetime

from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    title_en = models.CharField('Название на английском',
                                max_length=200,
                                blank=True)
    title_jp = models.CharField('Название на японском',
                                max_length=200,
                                blank=True)
    description = models.TextField('Описание', blank=True)
    img = models.ImageField('Изображение', null=True)
    previous_evolution = models.ForeignKey('self',
                                           verbose_name="Из кого эволюционировал",
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                verbose_name='Покемон',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    lat = models.FloatField('Долгота')
    lon = models.FloatField('Широта')

    appeared_at = models.DateTimeField('Появился', null=True, blank=True)
    disappeared_at = models.DateTimeField('Исчез', null=True, blank=True)

    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    attack = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
