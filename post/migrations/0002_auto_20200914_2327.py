# Generated by Django 3.0.6 on 2020-09-14 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='down_vote',
            field=models.ManyToManyField(blank=True, related_name='up', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='up_vote',
            field=models.ManyToManyField(blank=True, related_name='down', to=settings.AUTH_USER_MODEL),
        ),
    ]
