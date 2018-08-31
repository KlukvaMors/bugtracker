# Generated by Django 2.1 on 2018-08-30 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker_app', '0015_issuecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='api_key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
