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


# Exibir o perfil
@login_required
def profile_view(request):
    profile = request.user.profile
   
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'account/profile.html', {'profile': profile, 'users': users})

# Editar o perfil
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
            return redirect('profile_view')  
        else:
            return HttpResponse("Nenhuma imagem foi enviada", status=400)
    return redirect('profile_view')  

@login_required
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    
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
def edit_hard_skills(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        hard_skills_ids = request.POST.getlist('hard_skills')  # IDs das habilidades selecionadas
        if hard_skills_ids:
            hard_skills = Skill.objects.filter(id__in=hard_skills_ids)  # Filtra as skills válidas
            profile.hard_skills.set(hard_skills)  # Atualiza no perfil
            messages.success(request, "Hard skills atualizadas com sucesso!")
        else:
            profile.hard_skills.clear()  # Limpa se nada foi selecionado
            messages.info(request, "Nenhuma hard skill selecionada. Lista limpa.")
        return redirect('profile_view')

    return redirect('profile_view')