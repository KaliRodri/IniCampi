from django import forms
from feed.models import Profile, Skill

class ProfileForm(forms.ModelForm):
    hard_skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    # Limite para o campo 'summary'
    summary = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': '170'}),  # Limita a 100 caracteres no frontend
        max_length=170,  # Limita a 100 caracteres no backend
        required=False
    )

    class Meta:
        model = Profile
        fields = ['summary', 'hard_skills']
        widgets = {
            'hard_skills': forms.CheckboxSelectMultiple,
        }

    def clean_hard_skills(self):
        hard_skills = self.cleaned_data.get('hard_skills')
        
        # Validando a quantidade de hard skills selecionadas
        if len(hard_skills) < 6:
            raise forms.ValidationError("Você precisa selecionar pelo menos 6 habilidades.")
        if len(hard_skills) > 6:
            raise forms.ValidationError("Você pode selecionar no máximo 6 habilidades.")
        
        return hard_skills
