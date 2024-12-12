from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feed.models import Profile
from .forms import ProfileForm
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from feed.models import Project, Skill


# Exibir o perfil@login_required@login_required
@login_required
def profile_view(request):
    
    profile = request.user.profile

    # Verifica se o usuário é professor ou estudante
    teacher_projects = profile.created_projects.all() if profile.is_teacher() else None
    student_projects = profile.joined_projects.all() if profile.is_student() else None

    # Pesquisa por contatos
    query = request.GET.get('q', '')  # Obtém o parâmetro 'q' da URL
    if query:
        users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
        messages.info(request, f"Resultados para '{query}': {users.count()} usuário(s) encontrado(s).")
    else:
        users = User.objects.exclude(id=request.user.id)

    skills = Skill.objects.all()

    return render(request, 'account/profile.html', {
        'profile': profile,
        'teacher_projects': teacher_projects,
        'student_projects': student_projects,
        'users': users,
        'skills': skills,
        'query': query,
    })

    
# Editar o perfil
@login_required
def edit_profile(request):
    profile = request.user.profile
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'account/edit_profile.html', {'form': form, 'skills': skills, 'profile': profile})

@login_required
def edit_avatar(request):
    profile = request.user.profile 
    if request.method == 'POST':
        # Verifica se há um arquivo de imagem enviado
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
            profile.save()  
            return redirect('profile')  
    return redirect('profile')  

@login_required
def edit_background(request):
    profile = request.user.profile  
    if request.method == 'POST':
        # Verifica se há um arquivo de imagem enviado
        if 'profile_background_image' in request.FILES:
            profile.profile_background_image = request.FILES['profile_background_image']
            profile.save()  
            return redirect('profile')  
        else:
            return HttpResponse("Nenhuma imagem foi enviada", status=400)
    return redirect('profile')  

@login_required
def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    
    if request.method == 'POST':
        # Atualiza o resumo, se enviado
        if 'summary' in request.POST:
            profile.user.summary = request.POST['summary']
            profile.user.save()

        # Atualiza as hard skills, se enviadas
        if 'hard_skills' in request.POST:
            selected_skill = request.POST.get('hard_skills')
            if selected_skill in dict(Profile.HARD_SKILL_CHOICES).keys():
                profile.hard_skills = selected_skill
                profile.save()
        
        return redirect('profile', username=username)

    return render(request, 'account/profile.html', {'profile': profile})

@login_required
def unsubscribe_from_project(request, project_id):
    profile = request.user.profile
    project = get_object_or_404(Project, id=project_id)
    
    if profile in project.students.all():
        project.students.remove(profile)
    
    return redirect(reverse('profile'))

@login_required
def student_projects_view(request):
    profile = request.user.profile
    if profile.is_teacher:
        return redirect('teacher_projects_view')
    
    joined_projects = profile.joined_projects.all()
    return render(
        request,
        'account/student_projects.html',
        {'projects': joined_projects}
    )

@login_required
def teacher_projects_view(request):
    profile = request.user.profile
    if not profile.is_teacher:
        return redirect('student_projects_view')
    
    created_projects = profile.created_projects.all()
    return render(
        request,
        'account/teacher_projects.html',
        {'projects': created_projects}
    )
    
@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)  # Obtém o perfil do usuário logado

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'account/edit_profile.html', {'form': form})