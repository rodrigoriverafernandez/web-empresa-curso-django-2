# Generated by Django 2.0.2 on 2018-05-22 22:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 22, 53, 55, 687402, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
