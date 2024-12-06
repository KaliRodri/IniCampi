# views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Project, Comment
from .forms import CommentForm
from .forms import ProjectForm
from django.http import Http404
from django.db.models import Q


@login_required
def add_project(request):
    if request.user.profile.role != 'teacher':
        return redirect('home')  # Redireciona caso o usuário não seja professor

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user.profile  # Define o autor como o professor logado
            project.save()
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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Captura o parâmetro de pesquisa na URL
        if query:
            # Filtra projetos com base no título, corpo ou autor
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(author__user__username__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Inclui o formulário de comentário no contexto
        context['query'] = self.request.GET.get('q', '')  # Inclui a query no contexto para o formulário de pesquisa
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

# Função para que alunos se inscrevam nos projetos
@login_required
def join_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Verifica se o usuário é um aluno
    if request.user.profile.role != 'student':
        return redirect('home')  # Redireciona caso o usuário não seja aluno
    # Verifica se o aluno já está inscrito no projeto
    if request.user.profile in project.students.all():
        return redirect('home')  # Caso já tenha ingressado, redireciona de volta
    # Adiciona o aluno ao projeto
    student_profile = request.user.profile
    project.students.add(student_profile)  # Adiciona o aluno ao campo 'students' do projeto
    return redirect('home')  # Redireciona para a página inicial ou para os detalhes do projeto, se necessário

def edit_project(request, project_id):
    # Carrega o projeto a ser editado
    project = get_object_or_404(Project, id=project_id)

    # Verifica se o usuário é o autor (professor) do projeto
    if project.author.user != request.user:
        raise Http404("Você não tem permissão para editar este projeto.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página de detalhes do projeto após salvar
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

@login_required
def delete_comment(request, project_id, comment_id):
    # Obter o projeto e o comentário
    project = get_object_or_404(Project, id=project_id)
    comment = get_object_or_404(Comment, id=comment_id)

    # Verificar permissões: 
    # 1. O usuário é autor do comentário (alunos podem apagar seus próprios)
    # 2. O usuário é professor e autor do projeto
    if request.user.profile == comment.author or (
        request.user.profile.role == 'teacher' and project.author == request.user.profile
    ):
        comment.delete()
    else:
        messages.error(request, "Você não tem permissão para excluir este comentário.")

    # Redirecionar para a página de detalhes do projeto
    return redirect('home')