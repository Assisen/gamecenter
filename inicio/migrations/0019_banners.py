# Generated by Django 2.2.1 on 2019-08-22 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0018_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(null=True, upload_to='banners/', verbose_name='Banner')),
                ('createdat', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ['-createdat'],
            },
        ),
    ]
