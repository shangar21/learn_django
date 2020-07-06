# Generated by Django 3.0.7 on 2020-07-03 22:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200703_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podder',
            name='podder_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 22, 57, 52, 788595, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume_data',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 22, 57, 52, 787964, tzinfo=utc), verbose_name='Date Published'),
        ),
    ]
