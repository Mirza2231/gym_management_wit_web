from django.shortcuts import render, redirect
from django.urls import resolve
from django.http import JsonResponse
from .models import *
from .forms import ContactForm
from django.contrib import messages
import sweetify

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

# def gym_web_index(request):
#     return render(request, 'web_index.html')

# def gym_web_index(request):
#     return render(request, 'web_index.html')