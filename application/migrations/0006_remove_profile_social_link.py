# Generated by Django 4.1.5 on 2023-01-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_rename_date_joinnameed_user_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_link',
        ),
    ]
