# Generated by Django 3.0.5 on 2020-04-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20200419_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/d.png', upload_to='post_img/'),
        ),
    ]
