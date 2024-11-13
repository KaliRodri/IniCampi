from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    summary = models.TextField(blank=True, null=True)  # Adiciona o campo summary
    # outros campos do perfil, se houver

# Create your models here.
