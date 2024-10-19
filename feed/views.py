from django.shortcuts import render
from .models import Project, Teacher
from django.views import generic

# Create your views here.
def index(request):
    pass

class ProjectsListView(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'feed/projects_list.html'
    
class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 10
    template_name = 'feed/teacher_list.html'
    
class ProjectDetailView(generic.ListView):
    model = Project
    template_name = 'feed/projects_detail.html'

class TeacherDetailView(generic.ListView):
    model = Project
    template_name = 'feed/teacher_detail.html'

