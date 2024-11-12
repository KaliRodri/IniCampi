from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    matricula = models.CharField(max_length=9, validators=[MinLengthValidator(9)], unique=False)
    summary = models.TextField(max_length=500, help_text="Descreva seus conhecimentos aqui")
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    profile_background_image = models.ImageField(upload_to='profile_backgrounds/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Project(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=750, help_text="Descreva seu post aqui")
    calendar = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Profile, limit_choices_to={'role': 'teacher'}, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, limit_choices_to={'role': 'student'},on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.project.title}"
