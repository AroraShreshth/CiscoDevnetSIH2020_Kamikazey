# Generated by Django 2.2.10 on 2020-08-01 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0029_auto_20200802_0038'),
    ]

    operations = [
        migrations.AlterField(model_name='filehash', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 0, 39, 42, 883675)),),
    ]
