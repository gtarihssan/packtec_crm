# Generated by Django 4.1.3 on 2023-04-12 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_employer_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='date_creation',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='leave_days_number',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='username',
        ),
        migrations.AddField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
