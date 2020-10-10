# Generated by Django 3.0.6 on 2020-09-14 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_subcommunity_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcommunity',
            name='sub_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.SubCommunity'),
        ),
        migrations.AlterField(
            model_name='subcommunity',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community'),
        ),
    ]
