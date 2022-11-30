from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField('Название', max_length=200)
    img = models.ImageField('Изображение', null=True)

    def __str__(self):
        return self.title