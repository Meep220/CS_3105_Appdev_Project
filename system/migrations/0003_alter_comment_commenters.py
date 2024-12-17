# Generated by Django 4.2.13 on 2024-08-08 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenters', to=settings.AUTH_USER_MODEL),
        ),
    ]