# Generated by Django 3.1.4 on 2020-12-24 19:23

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_image_member),
        ),
    ]
