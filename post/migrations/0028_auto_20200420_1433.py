# Generated by Django 3.0.5 on 2020-04-20 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_auto_20200420_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 33, 11, 488390)),
        ),
    ]
