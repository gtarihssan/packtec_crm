# Generated by Django 4.1.3 on 2023-04-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_employer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='leave_days',
        ),
    ]