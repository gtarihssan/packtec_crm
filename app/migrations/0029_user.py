# Generated by Django 4.2 on 2023-04-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_holidays_unpaid_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
