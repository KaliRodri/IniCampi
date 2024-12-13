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
from django.contrib import messages


@login_required
def add_project(request):
    if request.user.profile.role != 'teacher':
        return redirect('home')  

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user.profile  
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
        query = self.request.GET.get('q')  
        if query:
            
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(author__user__username__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  
        context['query'] = self.request.GET.get('q', '')  
        return context


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
            return redirect('home')  
    return redirect('home')  

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    is_author = hasattr(request.user, 'profile') and project.author == request.user.profile
    is_admin = request.user.is_staff
    
    if is_author or is_admin:
        project.delete()
    
    return redirect('home')  


@login_required
def join_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    
    if request.user.profile.role != 'student':
        return redirect('home')  
   
    if request.user.profile in project.students.all():
        return redirect('home')  
    
    student_profile = request.user.profile
    project.students.add(student_profile)  
    return redirect('home') 

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    
    if project.author.user != request.user:
        raise Http404("Você não tem permissão para editar este projeto.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

@login_required
def delete_comment(request, project_id, comment_id):
    
    project = get_object_or_404(Project, id=project_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user.profile == comment.author or (
        request.user.profile.role == 'teacher' and project.author == request.user.profile
    ):
        comment.delete()
    else:
        messages.error(request, "Você não tem permissão para excluir este comentário.")

    return redirect('home')