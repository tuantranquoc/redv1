# Generated by Django 3.0.6 on 2020-10-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id']},
        ),
    ]
