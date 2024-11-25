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
    list_display = ('user', 'role', 'matricula', 'summary', 'get_hard_skills')
    inlines = [ProjectInLine, CommentInLine]
    def get_hard_skills(self, obj):
        return ", ".join([skill.name for skill in obj.hard_skills.all()])
    get_hard_skills.short_description = 'Hard Skills'
    list_filter = ('role',)    