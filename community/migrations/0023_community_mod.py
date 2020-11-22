# Generated by Django 3.0.7 on 2020-11-21 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0022_auto_20201121_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='mod',
            field=models.ManyToManyField(blank=True, related_name='mod', to=settings.AUTH_USER_MODEL),
        ),
    ]
