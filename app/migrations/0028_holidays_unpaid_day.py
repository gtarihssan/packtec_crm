# Generated by Django 4.2 on 2023-04-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_holidays_days_number_holidays_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidays',
            name='unpaid_day',
            field=models.IntegerField(default=0),
        ),
    ]
