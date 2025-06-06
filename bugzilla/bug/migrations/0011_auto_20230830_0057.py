# Generated by Django 3.2 on 2023-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0010_alter_bug_bug_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='bug_status',
            field=models.CharField(choices=[('new', 'NEW'), ('started', 'STARTED'), ('completed', 'COMPLETED'), ('resolved', 'RESOLVED')], max_length=10),
        ),
        migrations.AlterField(
            model_name='bug',
            name='bug_type',
            field=models.CharField(choices=[('feature', 'FEATURE'), ('bug', 'BUG')], max_length=10),
        ),
    ]
