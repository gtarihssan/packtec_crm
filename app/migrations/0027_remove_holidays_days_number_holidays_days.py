# Generated by Django 4.2 on 2023-04-26 08:10

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_holidays_weekends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidays',
            name='days_number',
        ),
        migrations.AddField(
            model_name='holidays',
            name='days',
            field=app.models.ListField(default=[]),
        ),
    ]
