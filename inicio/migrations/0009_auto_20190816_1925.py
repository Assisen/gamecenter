# Generated by Django 2.2.1 on 2019-08-17 00:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_auto_20190816_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='producto',
            field=models.ForeignKey(on_delete='cascade', to='inicio.Producto'),
        ),
        migrations.AlterField(
            model_name='favorito',
            name='user',
            field=models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]
