# Generated by Django 5.1 on 2024-10-25 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_remove_teacher_project_project_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='teacher',
        ),
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='feed.teacher'),
        ),
    ]