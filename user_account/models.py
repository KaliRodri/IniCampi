from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    summary = models.TextField(blank=True, null=True)

    hard_skills = models.CharField(max_length=200, blank=True, null=True)

# Create your models here.
