# Generated by Django 5.1 on 2024-11-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_profile_hard_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], default='student', max_length=7),
        ),
    ]
