# Generated by Django 3.0.6 on 2020-09-28 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='tweet',
            new_name='post',
        ),
    ]
