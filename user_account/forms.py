from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = ['summary', 'profile_image', 'profile_background_image']