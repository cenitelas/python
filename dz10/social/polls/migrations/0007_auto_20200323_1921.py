# Generated by Django 3.0.4 on 2020-03-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200323_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='', max_length=200, upload_to='profile_images/'),
        ),
    ]
