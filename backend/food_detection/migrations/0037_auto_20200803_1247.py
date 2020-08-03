# Generated by Django 2.2.10 on 2020-08-03 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0036_auto_20200803_1232'),
    ]

    operations = [
        migrations.RemoveField(model_name='alert', name='url',),
        migrations.AddField(model_name='alert', name='URL', field=models.URLField(default=''), preserve_default=False,),
        migrations.AlterField(model_name='alert', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 12, 47, 35, 877693)),),
    ]
