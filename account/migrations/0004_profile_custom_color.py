# Generated by Django 3.0.7 on 2020-11-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='custom_color',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.CustomColor'),
        ),
    ]
