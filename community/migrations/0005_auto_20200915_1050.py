# Generated by Django 3.0.6 on 2020-09-15 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20200915_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='join',
            new_name='user',
        ),
    ]
