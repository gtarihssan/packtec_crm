# Generated by Django 4.2 on 2023-04-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_holidays_days_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='mdp',
            field=models.CharField(default='', max_length=50),
        ),
    ]
