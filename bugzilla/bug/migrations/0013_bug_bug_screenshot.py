# Generated by Django 3.2 on 2023-08-30 10:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0012_alter_bug_bug_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='bug_screenshot',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
