from django.contrib import admin
from feed.models import Student, Project, Comment, Teacher
# Register your models here.

class ProjectInLine(admin.TabularInline): 
    model = Project
    extra = 0
    fields = ('title', 'body', 'calendar')
    
class CommentInLine(admin.TabularInline): 
    model = Comment
    extra = 0
    fields = ('author', 'body')
    
class TeacherInLine(admin.TabularInline): 
    model = Teacher
    extra = 0

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'user_name', 'summary')
    inlines = [ProjectInLine]
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'user_name', 'summary')
    inlines = [CommentInLine]



    
