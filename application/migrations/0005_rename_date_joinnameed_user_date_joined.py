# Generated by Django 4.1.5 on 2023-01-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_remove_user_date_joined_user_date_joinnameed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_joinnameed',
            new_name='date_joined',
        ),
    ]
