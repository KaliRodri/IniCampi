# Generated by Django 5.1.2 on 2024-11-12 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_alter_profile_profile_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'student'}, related_name='joined_projects', to='feed.profile'),
        ),
    ]
