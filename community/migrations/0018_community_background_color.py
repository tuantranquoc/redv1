# Generated by Django 3.0.7 on 2020-11-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_auto_20201106_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='background_color',
            field=models.TextField(default='#30363C'),
        ),
    ]