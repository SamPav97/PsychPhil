# Generated by Django 4.1.3 on 2022-11-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapies', '0002_alter_therapy_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapy',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
