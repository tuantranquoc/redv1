# Generated by Django 3.0.7 on 2020-11-18 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0018_community_background_color'),
        ('track', '0008_auto_20201118_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communitytrack',
            name='community',
        ),
        migrations.AddField(
            model_name='communitytrack',
            name='community',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community'),
        ),
    ]
