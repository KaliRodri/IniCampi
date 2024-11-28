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



@login_required
def profile_view(request):
    profile = request.user.profile
<<<<<<< HEAD
    
    if profile.role == 'student':
        student_projects = profile.joined_projects.all()  
        teacher_projects = None 

    
    elif profile.role == 'teacher':
        student_projects = None  
        teacher_projects = Project.objects.filter(author=profile)  
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'account/profile.html', {'profile': profile,'student_projects': student_projects,
        'teacher_projects': teacher_projects, 'users': users})

=======
    users = User.objects.exclude(id=request.user.id)
    skills = Skill.objects.all()  # Passa todas as skills para o dropdown
    return render(request, 'account/profile.html', {
        'profile': profile,
        'users': users,
        'skills': skills,
    })
>>>>>>> 734cc8be799c43f8395fe5eaad1b67f11a7a6df0

@login_required
def edit_profile(request):
    profile = request.user.profile
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'account/edit_profile.html', {'form': form, 'skills': skills, 'profile': profile})

@login_required
def edit_avatar(request):
    profile = request.user.profile 
    if request.method == 'POST':
        
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
            profile.save()  
            return redirect('profile')  
    return redirect('profile')  

@login_required
def edit_background(request):
    profile = request.user.profile  
    if request.method == 'POST':
        
        if 'profile_background_image' in request.FILES:
            profile.profile_background_image = request.FILES['profile_background_image']
            profile.save()  
            return redirect('profile_view')  
        else:
            return HttpResponse("Nenhuma imagem foi enviada", status=400)
    return redirect('profile_view')  

@login_required
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    
    if request.method == 'POST':
        
        if 'summary' in request.POST:
            profile.user.summary = request.POST['summary']
            profile.user.save()

       
        if 'hard_skills' in request.POST:
            selected_skill = request.POST.get('hard_skills')
            if selected_skill in dict(Profile.HARD_SKILL_CHOICES).keys():
                profile.hard_skills = selected_skill
                profile.save()
        
        return redirect('profile', username=username)

    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_summary(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.summary = request.POST.get('summary')
        profile.save()
        return redirect('profile')  
    return render(request, 'profile.html')

@login_required
def unsubscribe_from_project(request, project_id):
    profile = request.user.profile
    project = get_object_or_404(Project, id=project_id)
    
    if profile in project.students.all():
        project.students.remove(profile)
    
    return redirect(reverse('profile_view'))

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
def edit_hard_skills(request):
    profile = get_object_or_404(Profile, user=request.user)
<<<<<<< HEAD
    if request.method == "POST":
        hard_skills_ids = request.POST.getlist('hard_skills')  
        if hard_skills_ids:
            hard_skills = Skill.objects.filter(id__in=hard_skills_ids)  
            profile.hard_skills.set(hard_skills)  
            messages.success(request, "Hard skills atualizadas com sucesso!")
        else:
            profile.hard_skills.clear()  
            messages.info(request, "Nenhuma hard skill selecionada. Lista limpa.")
=======
    
    if request.method == 'POST':
        # Remover skill selecionada
        if 'remove_skill' in request.POST:
            skill_id = request.POST['remove_skill']
            skill = get_object_or_404(Skill, id=skill_id)
            profile.hard_skills.remove(skill)
            messages.success(request, f"Skill '{skill.name}' removida com sucesso.")
        
        # Adicionar nova skill, se fornecida
        if 'new_skill' in request.POST and request.POST['new_skill'].strip():
            new_skill_name = request.POST['new_skill'].strip()
            skill, created = Skill.objects.get_or_create(name=new_skill_name)
            profile.hard_skills.add(skill)
            if created:
                messages.success(request, f"Nova skill '{skill.name}' adicionada com sucesso.")
            else:
                messages.info(request, f"A skill '{skill.name}' já existe e foi adicionada ao seu perfil.")
        
>>>>>>> 734cc8be799c43f8395fe5eaad1b67f11a7a6df0
        return redirect('profile_view')

    return redirect('profile_view')