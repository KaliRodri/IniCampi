from django import forms
from feed.models import Profile, Skill

class ProfileForm(forms.ModelForm):
    hard_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    
    summary = forms.CharField(
        widget=forms.Textarea(attrs={
            'maxlength': '170',
            'placeholder': 'Escreva sobre um pouco você',
            'class': 'form-control'
        }),
        max_length=170,
        required=False
    )

    class Meta:
        model = Profile
        fields = ['summary', 'hard_skills', 'contact_number']

    def clean_hard_skills(self):
        hard_skills = self.cleaned_data.get('hard_skills')
        
       
        if len(hard_skills) < 6:
            raise forms.ValidationError("Você precisa selecionar pelo menos 6 habilidades.")
        if len(hard_skills) > 6:
            raise forms.ValidationError("Você pode selecionar no máximo 6 habilidades.")
        
        return hard_skills
