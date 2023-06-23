# Generated by Django 2.0.2 on 2018-05-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='link',
        ),
        migrations.AddField(
            model_name='service',
            name='subtitle',
            field=models.CharField(default=0, max_length=200, verbose_name='Subtitulo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo '),
        ),
    ]