# Generated by Django 5.1.2 on 2024-12-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0017_alter_project_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
