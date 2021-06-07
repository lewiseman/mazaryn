# Generated by Django 3.2.3 on 2021-06-07 12:48

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210606_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=profiles.models.upload_avatar, upload_to='avatars/'),
        ),
    ]