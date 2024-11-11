# views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Project, Comment
from .forms import CommentForm
from .forms import ProjectForm

@login_required
def add_project(request):
    if request.user.profile.role != 'teacher':
        return redirect('home')  # Redireciona caso o usuário não seja professor

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'feed/add_project.html', {'form': form})

class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'feed/feed.html'
    context_object_name = 'projects'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Inclui o formulário de comentário no contexto
        return context

# Função para adicionar comentários diretamente no feed
@login_required
def add_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.author = request.user.profile
            comment.save()
            return redirect('home')  # Redireciona para o feed após salvar o comentário
    return redirect('home')  # Redireciona para o feed mesmo em caso de erro

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    is_author = hasattr(request.user, 'profile') and project.author == request.user.profile
    is_admin = request.user.is_staff
    
    if is_author or is_admin:
        project.delete()
    
    return redirect('home')  # Redireciona após a exclusão
