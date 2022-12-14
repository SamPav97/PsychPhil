# Generated by Django 4.1.3 on 2022-12-04 17:13

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('therapies', '0005_alter_therapy_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapy',
            name='summary',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='therapy',
            name='therapists',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
