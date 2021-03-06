# Generated by Django 3.0.6 on 2020-10-05 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_remove_subcommunity_post'),
        ('post', '0008_auto_20201005_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community'),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.SubCommunity'),
        ),
    ]
