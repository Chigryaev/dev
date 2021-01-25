# Generated by Django 3.1.5 on 2021-01-25 18:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='total_likes',
            new_name='total_vote',
        ),
        migrations.RemoveField(
            model_name='article',
            name='users_like',
        ),
        migrations.AddField(
            model_name='article',
            name='users_vote',
            field=models.ManyToManyField(blank=True, related_name='post_vote', to=settings.AUTH_USER_MODEL),
        ),
    ]