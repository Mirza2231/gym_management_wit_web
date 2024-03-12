from django import forms
from .models import Trainer

class AddTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'contact', 'email', 'age','gender','instalink','xlink','facebooklink','profile_pic']
        
class TrainerEditForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'contact', 'email', 'age','gender','instalink','xlink','facebooklink','profile_pic'] 