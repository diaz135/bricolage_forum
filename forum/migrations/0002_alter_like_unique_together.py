# Generated by Django 5.1.2 on 2024-11-01 07:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('publication', 'user')},
        ),
    ]
