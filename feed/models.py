from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Student(models.Model):
       matricula = models.CharField(
        max_length=9,  # Garante que não exceda 9 caracteres
        validators=[MinLengthValidator(9)],  # Garante que tenha no mínimo 9 caracteres
        primary_key=True,
        help_text="Entre com sua matrícula"
    )
       password = models.CharField(max_length=6, help_text="Entre com os seis primeiros dígitos do seu cpf")
       user_name = models.CharField(max_length=30)
       summary = models.TextField(max_length=750, help_text=("Descreva seus conhecimentos aqui"))
       
       def __str__(self):
        return self.matricula
       
class Teacher(models.Model):
    matricula = models.CharField(
        max_length=9,  
        validators=[MinLengthValidator(9)],  
        primary_key=True,
        help_text="Entre com sua matrícula"
    )
    password = models.CharField(max_length=6, help_text="Entre com os seis primeiros dígitos do seu cpf")
    user_name = models.CharField(max_length=30)
    summary = models.TextField(max_length=750, help_text="Descreva seus conhecimentos aqui")
    
    def __str__(self):
        return self.matricula

class Project(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=750, help_text="Descreva seu post aqui")
    calendar = models.DateField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher,related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Student, related_name='comments', on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.project.title}"
       

