# Generated by Django 2.1.11 on 2020-02-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboPortal', '0002_token_userlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='portaluser',
            name='joined_team',
            field=models.BooleanField(default=False),
        ),
    ]
