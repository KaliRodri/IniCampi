from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='student')
    matricula = models.CharField(max_length=9, validators=[MinLengthValidator(9)], unique=False)
    summary = models.TextField(max_length=500, help_text="Descreva seus conhecimentos aqui")
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    profile_background_image = models.ImageField(upload_to='profile_backgrounds/', null=True, blank=True)
    hard_skills = models.ManyToManyField(Skill, blank=True)
    contact_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'O número de contato deve estar no formato: "999999999". Até 15 dígitos permitidos.')]
    )
    
    def is_teacher(self):
        return self.role == 'teacher'

    def is_student(self):
        return self.role == 'student'
    
    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Project(models.Model):
    OPEN_STATUS = True
    CLOSED_STATUS = False

    STATUS_CHOICES = (
        (OPEN_STATUS, 'Aberto'),
        (CLOSED_STATUS, 'Fechado'),
    )

    title = models.CharField(max_length=100)
    body = models.TextField(max_length=750)
    calendar = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        Profile, 
        limit_choices_to={'role': 'teacher'}, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='created_projects'
    )
    students = models.ManyToManyField(
        Profile, 
        related_name='joined_projects', 
        limit_choices_to={'role': 'student'}, 
        blank=True
    )
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='project_pdfs/', null=True, blank=True)
    status = models.BooleanField(default=OPEN_STATUS, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, limit_choices_to={'role': 'student'},on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.project.title}"
