# Generated by Django 4.1.5 on 2023-02-09 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_alter_post_conteudo_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 2, 9, 23, 34, 37, 858630, tzinfo=datetime.timezone.utc)),
        ),
    ]