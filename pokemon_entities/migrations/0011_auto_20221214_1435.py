# Generated by Django 3.1.14 on 2022-12-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20221214_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]