# Generated by Django 4.1.3 on 2022-11-18 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='date_joined',
        ),
    ]
