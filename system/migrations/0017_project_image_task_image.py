# Generated by Django 4.2.13 on 2024-08-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_remove_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/projects/'),
        ),
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/projects/'),
        ),
    ]