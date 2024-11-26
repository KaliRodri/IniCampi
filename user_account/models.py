from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    summary = models.TextField(blank=True, null=True)
    
    hard_skills = models.ManyToManyField(Skill, blank=True)

# Create your models here.
