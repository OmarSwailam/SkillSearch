# Generated by Django 4.1.5 on 2023-02-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_alter_project_image_alter_project_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.png', upload_to='projects/'),
        ),
    ]