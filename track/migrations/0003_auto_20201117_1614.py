# Generated by Django 3.0.7 on 2020-11-17 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20201117_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitytrack',
            old_name='comunity',
            new_name='community',
        ),
    ]
