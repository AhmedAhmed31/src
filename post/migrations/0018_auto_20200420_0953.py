# Generated by Django 3.0.5 on 2020-04-20 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20200420_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 9, 53, 30, 843059)),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/default.png', null=True, upload_to='post_img/'),
        ),
    ]
