from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from feed.models import Profile
from .forms import ProfileForm

# Exibir o perfil
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'account/profile.html', {'profile': profile})

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

