# Generated by Django 4.1.7 on 2023-03-21 07:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue_tracker', '0008_issue_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]