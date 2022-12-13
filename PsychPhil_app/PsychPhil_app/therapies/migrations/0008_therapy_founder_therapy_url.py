# Generated by Django 4.1.3 on 2022-12-05 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0007_alter_therapy_therapists'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapy',
            name='founder',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapy',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
