from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feed.models import Profile
from .forms import ProfileForm
from django.http import HttpResponse

# Exibir o perfil
@login_required
def profile_view(request):
    profile = request.user.profile
    # Obtém todos os usuários do sistema, exceto o próprio usuário logado
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'account/profile.html', {'profile': profile, 'users': users})

# Editar o perfil
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'account/edit_profile.html', {'form': form})

@login_required
def edit_avatar(request):
    profile = request.user.profile  # Obtém o perfil do usuário logado
    if request.method == 'POST':
        # Verifica se há um arquivo de imagem enviado
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
            profile.save()  # Salva a nova imagem no perfil
            return redirect('profile')  # Redireciona para a página de perfil
    return redirect('profile')  # Caso não tenha enviado nada, apenas redireciona

@login_required
def edit_background(request):
    profile = request.user.profile  # Obtém o perfil do usuário logado
    if request.method == 'POST':
        # Verifica se há um arquivo de imagem enviado
        if 'profile_background_image' in request.FILES:
            profile.profile_background_image = request.FILES['profile_background_image']
            profile.save()  # Salva a nova imagem no perfil
            return redirect('profile_view')  # Redireciona para a página de perfil
        else:
            return HttpResponse("Nenhuma imagem foi enviada", status=400)
    return redirect('profile_view')  # Caso não tenha enviado nada, apenas redireciona

@login_required
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    
    if request.method == 'POST' and 'summary' in request.POST:
        profile.user.summary = request.POST['summary']
        profile.user.save()
        return redirect('profile', username=username)
    
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_summary(request):
    if request.method == 'POST':
        summary = request.POST.get('summary')
        request.user.profile.summary = summary
        request.user.profile.save()
        return redirect('profile')
    return redirect('profile')