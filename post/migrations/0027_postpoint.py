# Generated by Django 3.0.6 on 2020-11-05 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_auto_20201105_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.FloatField(default=0)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
            options={
                'ordering': ['-point'],
            },
        ),
    ]
