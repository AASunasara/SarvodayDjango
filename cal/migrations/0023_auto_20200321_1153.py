# Generated by Django 3.0.3 on 2020-03-21 06:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cal', '0022_auto_20200316_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='factorylog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, unique=True)),
                ('fact_open_time', models.TimeField(default='10:00 AM')),
                ('fact_close_time', models.TimeField(blank=True, default='10:00 PM', null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, max_length=1000, null=True)),
                ('setup', models.TextField(blank=True, max_length=1000, null=True)),
                ('cleansing', models.TextField(blank=True, max_length=1000, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='items',
            name='note',
        ),
        migrations.DeleteModel(
            name='days',
        ),
    ]
