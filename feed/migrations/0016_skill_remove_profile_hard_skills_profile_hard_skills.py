# Generated by Django 5.1.2 on 2024-11-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_project_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hard_skills',
        ),
        migrations.AddField(
            model_name='profile',
            name='hard_skills',
            field=models.ManyToManyField(blank=True, to='feed.skill'),
        ),
    ]
