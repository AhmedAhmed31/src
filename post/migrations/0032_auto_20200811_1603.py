# Generated by Django 3.0.5 on 2020-08-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0031_auto_20200624_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='post_img/'),
        ),
    ]
