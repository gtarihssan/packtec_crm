# Generated by Django 4.1.3 on 2023-04-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_employer_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='direction',
            field=models.CharField(choices=[('DT', 'DT'), ('DTE', 'DTE'), ('PAC', 'PAC'), ('DAF', 'DAF')], max_length=50, null=True),
        ),
    ]
