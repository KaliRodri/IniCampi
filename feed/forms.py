from django import forms
from .models import Comment, Project

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-field',  
                'placeholder': 'Escreva um comentário...',
                'rows': 3,
            }),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'body', 'calendar', 'image', 'pdf_file', 'status']  
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-field',
                'placeholder': 'Título do Projeto',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-field',
                'placeholder': 'Descrição do Projeto',
                'rows': 3,
            }),
            'calendar': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-field',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-field',
            }),
            'pdf_file': forms.ClearableFileInput(attrs={  
                'class': 'form-field',
            }),
            'status': forms.Select(attrs={
                'class': 'form-field',  
            }),
        }
        labels = {
            'title': '',  
            'body': '',
            'calendar': '',
            'image': 'Foto da IC',
            'pdf_file': 'Ementa do IC',  
            'status': 'Status',  
        }
