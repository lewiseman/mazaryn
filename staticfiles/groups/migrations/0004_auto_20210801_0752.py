# Generated by Django 3.2.4 on 2021-08-01 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('groups', '0003_group_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='admin',
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_admin', to='profiles.profile'),
        ),
    ]
