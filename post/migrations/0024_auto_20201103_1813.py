# Generated by Django 3.0.6 on 2020-11-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20201103_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
    ]
