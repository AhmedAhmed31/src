# Generated by Django 3.0.5 on 2020-04-20 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 35, 18, 234148)),
        ),
    ]
