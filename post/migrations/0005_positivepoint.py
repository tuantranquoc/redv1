# Generated by Django 3.0.6 on 2020-09-15 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_delete_positivepoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositivePoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('point', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
