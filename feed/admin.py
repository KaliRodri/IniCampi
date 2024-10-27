from django.contrib import admin
from feed.models import Profile, Project, Comment
# Register your models here.

class ProjectInLine(admin.TabularInline): 
    model = Project
    extra = 0
    fields = ('title', 'body', 'calendar')
    
class CommentInLine(admin.TabularInline): 
    model = Comment
    extra = 0
    fields = ('author', 'body')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'matricula', 'summary')
    inlines = [ProjectInLine, CommentInLine]
    list_filter = ('role',)    