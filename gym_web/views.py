from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.contrib import messages
import sweetify
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .forms import UserLoginForm
from django.contrib.auth import logout

# Create your views here.


def gym_web_index(request):
    return render(request, 'web_index.html')

def gym_web_service(request):
        return render(request, 'web_services.html')
             
def gym_web_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Your Submission Has Done Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
        else:
            # Return form errors
            # sweetify.error(request, 'Something Went Wrong Please Try Again Later') 
            messages.error(request, 'This is a success message!')    
             
              # Redirect to a success page after form submission
    else:
        form = ContactForm()
    return render(request, 'web_contact.html', {'form': form})

def gym_web_about(request):
    return render(request, 'web_about-us.html')

def gym_web_team(request):
    return render(request, 'web_team.html')

def gym_web_login(request):
    return render(request, 'web_login.html')

def gym_web_register(request):
    return render(request, 'web_register.html')

def signup(request):
    if request.method == 'POST':
        sign_form = SignUpForm(request.POST, request.FILES)
        if sign_form.is_valid():
             email = sign_form.cleaned_data.get('email')
             if User.objects.filter(email=email).exists():
                    sweetify.error(request, f"Email '{email}' already exists. Account not created.", timer=5000, timerProgressBar='true', persistent="Close")
             try:
                user = sign_form.save()
                father_name = sign_form.cleaned_data.get('father_name')
                gender = sign_form.cleaned_data.get('gender')
                profile_pic = sign_form.cleaned_data.get('profile_pic')
                UserProfile.objects.create(user=user, father_name=father_name, gender=gender, profile_pic=profile_pic)
                raw_password = sign_form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                sweetify.success(request, 'Welcome! Register Sucessfull', timer=5000, timerProgressBar='true', persistent="Close")
                return redirect('gym_web_index')  # Redirect to the homepage after successful signup
             except Exception as e: 
                sweetify.error(request, 'An error occurred please try again later', timer=5000, timerProgressBar='true', persistent="Close")
        else:
            errors = []
            for field_errors in sign_form.errors.values():
                errors.extend(field_errors)
                
            error_messages = "\n".join(errors)
            sweetify.error(request, f'{error_messages}', timer=5000, timerProgressBar='true', persistent="Close")
    else:
        sign_form = SignUpForm()
    return render(request, 'web_register.html', {'sign_form': sign_form})


def login_view(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gym_web_index')  # Redirect to the homepage after successful login
        else:
            # login_form.add_error(None, "Invalid username or password.")
            errors = []
            for field_errors in login_form.errors.values():
                errors.extend(field_errors)

            error_messages = "\n".join(errors)
            sweetify.error(request, f'{error_messages}', timer=5000, timerProgressBar='true', persistent="Close")
            # sweetify.error(request, f'{login_form.errors}', timer=5000, timerProgressBar='true', persistent="Close")
    else:
        login_form = UserLoginForm()
    return render(request, 'web_login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('gym_web_login')




