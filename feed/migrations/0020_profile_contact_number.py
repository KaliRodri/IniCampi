# Generated by Django 5.1 on 2024-12-12 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0019_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'O número de contato deve estar no formato: "999999999". Até 15 dígitos permitidos.')]),
        ),
    ]
