# Generated by Django 3.0.5 on 2020-04-20 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20200420_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 9, 52, 1, 222878)),
        ),
    ]
