# Generated by Django 4.1.3 on 2023-04-12 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_employer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='date_creation',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='photo',
        ),
    ]