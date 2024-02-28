# forms.py
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class SignUpForm(UserCreationForm):
    father_name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'father_name', 'gender', 'profile_pic', 'password1', 'password2')
        
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']