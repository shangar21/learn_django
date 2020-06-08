# Generated by Django 3.0.7 on 2020-06-08 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200608_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podder',
            name='podder_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 20, 12, 50, 335170, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 20, 12, 50, 334956, tzinfo=utc), verbose_name='Date Published'),
        ),
    ]