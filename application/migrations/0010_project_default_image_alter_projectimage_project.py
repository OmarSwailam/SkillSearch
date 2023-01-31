# Generated by Django 4.1.5 on 2023-01-31 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_remove_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='default_image',
            field=models.ImageField(default='images/default.png', editable=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='application.project'),
        ),
    ]