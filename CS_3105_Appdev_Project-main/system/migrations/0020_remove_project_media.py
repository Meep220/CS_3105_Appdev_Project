# Generated by Django 4.2.13 on 2024-08-29 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_project_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='media',
        ),
    ]
