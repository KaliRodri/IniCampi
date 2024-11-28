from django import forms
from feed.models import Profile, Skill

class ProfileForm(forms.ModelForm):
    hard_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        models = Profile
        fields = ['user.username', 'summary', 'profile_image', 'profile_background_image', 'hard_skills']
        widgets = {
            'hard_skills': forms.CheckboxSelectMultiple,  
        }
        