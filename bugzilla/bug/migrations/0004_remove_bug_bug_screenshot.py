# Generated by Django 3.2 on 2023-08-29 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_auto_20230829_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='bug_screenshot',
        ),
    ]
