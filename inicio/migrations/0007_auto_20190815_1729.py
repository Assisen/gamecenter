# Generated by Django 2.2.1 on 2019-08-15 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_auto_20190815_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo',
            field=models.FloatField(verbose_name='Costo'),
        ),
    ]
