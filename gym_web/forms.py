# forms.py
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm




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
        

class CustomPasswordChangeForm(PasswordChangeForm): 
    pass 


class ProfileEditForm(forms.ModelForm):
    father_name = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['father_name', 'gender', 'profile_pic']

    # Fields from the User model
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        if self.instance.user:
            user = self.instance.user
            self.fields['username'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit=True):
        user_profile = super(ProfileEditForm, self).save(commit=False)
        user = user_profile.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            user_profile.save()
        return user_profile