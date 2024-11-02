from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Project

# Create your views here.
class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'feed/feed.html'
    context_object_name = 'projects'
    # login_url = 'login' substituir pela url

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Verifica se o usuário tem um perfil ou se é um administrador
    is_author = hasattr(request.user, 'profile') and project.author == request.user.profile
    is_admin = request.user.is_staff
    
    if is_author or is_admin:  # Permite que o autor ou o administrador excluam o projeto
        project.delete()
    
    return redirect('home')  # Redireciona após a exclusão

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'feed/projects_detail.html'
    context_object_name = 'project'

