# Generated by Django 3.0.7 on 2020-11-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_community_background_color'),
        ('track', '0003_auto_20201117_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitytrack',
            name='community',
        ),
        migrations.AddField(
            model_name='communitytrack',
            name='community',
            field=models.ManyToManyField(blank=True, null=True, to='community.Community'),
        ),
    ]
