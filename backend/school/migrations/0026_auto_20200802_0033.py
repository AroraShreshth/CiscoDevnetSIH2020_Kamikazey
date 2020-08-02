# Generated by Django 2.2.10 on 2020-08-01 19:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0025_auto_20200801_2358'),
    ]

    operations = [
        migrations.AlterField(model_name='attendance', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 19, 3, 50, 834215, tzinfo=utc)),),
        migrations.AlterField(
            model_name='school', name='principal', field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='principal_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='school', name='under_supervisor', field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisor_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(model_name='wastage', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 19, 3, 50, 833218, tzinfo=utc)),),
    ]