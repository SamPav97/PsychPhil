# Generated by Django 4.1.3 on 2022-11-20 21:16

import PsychPhil_app.core.model_mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
            bases=(PsychPhil_app.core.model_mixins.StrFromFieldsMixin, models.Model),
        ),
    ]