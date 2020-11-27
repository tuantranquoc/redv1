# Generated by Django 3.0.7 on 2020-11-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0021_auto_20201121_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='background_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='button_background_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='button_text_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='description_background_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='post_background_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='text_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
        migrations.AlterField(
            model_name='community',
            name='title_background_color',
            field=models.CharField(default='#30363C', max_length=7),
        ),
    ]