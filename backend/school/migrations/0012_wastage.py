# Generated by Django 2.2.10 on 2020-08-01 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_fooditem_nutrition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wastage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('FoodSchedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.FoodSchedule')),
            ],
            options={'verbose_name': 'Food Wastage', 'verbose_name_plural': 'Food Wastages',},
        ),
    ]
