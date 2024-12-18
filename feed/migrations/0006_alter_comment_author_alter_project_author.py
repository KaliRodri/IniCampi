# Generated by Django 5.1 on 2024-10-27 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_rename_teacher_project_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'teacher'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.profile'),
        ),
    ]
