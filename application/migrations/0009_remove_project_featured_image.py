# Generated by Django 4.1.5 on 2023-01-29 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_rename_product_projectimage_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured_image',
        ),
    ]
