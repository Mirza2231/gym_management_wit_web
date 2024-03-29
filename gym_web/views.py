from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ContactForm
from django.contrib import messages
import sweetify
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm, BookingForm,BookingEditForm
from gym.models import *
from django import template



def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def gym_web_index(request):
    trainers = Trainer.objects.all()
    packages= MembershipPackage.objects.all()
    category = PCategory.objects.all() 
    return render(request, 'web_index.html', {'trainers': trainers, 'packages':packages, 'category':category})

def gym_web_service(request):
    trainers = Trainer.objects.all()
    packages= MembershipPackage.objects.all()
    category = PCategory.objects.all() 
    return render(request, 'web_services.html', {'trainers': trainers, 'packages':packages, 'category':category})
             
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
    trainers = Trainer.objects.all()
    return render(request, 'web_about-us.html', {'trainers': trainers,})

def gym_web_team(request):
    trainers = Trainer.objects.all()
    return render(request, 'web_team.html', {'trainers': trainers})

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



@login_required(login_url='/login/')
def profile_edit(request):
    if request.method == 'POST':
        pro_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        if pro_form.is_valid():
            pro_form.save()
            sweetify.success(request, 'Profile updated successfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('gym_web_index')  # Redirect to the user's profile page
        else:
            errors = []
            for field_errors in pro_form.errors.values():
                errors.extend(field_errors)
            error_messages = "\n".join(errors)
            sweetify.error(request, f'{error_messages}', timer=5000, timerProgressBar='true', persistent="Close")
    else:
        pro_form = ProfileEditForm(instance=request.user.userprofile)
    return render(request, 'web_proedit.html', {'pro_form': pro_form})


def login_view(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                sweetify.success(request,'Login Sucessfull', timer=5000, timerProgressBar='true', persistent="Close")
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

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('gym_web_login')

@login_required(login_url='/login/')
def password_change(request):
    if request.method == 'POST':
        cp_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if cp_form.is_valid():
            cp_form.save()
            sweetify.success(request,'Password Change Sucessfull', timer=5000, timerProgressBar='true', persistent="Close")
            # Update the session to prevent the user from being logged out
            update_session_auth_hash(request, cp_form.user)
            return redirect('gym_web_index')  # Redirect to the user's profile page
    else:
        cp_form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'web_changepass.html', {'cp_form': cp_form})

@login_required(login_url='/login/')
def book_time(request, package_id):
    package = MembershipPackage.objects.get(id=package_id)
    shifts = Shifts.objects.all()  # Fetch all shifts
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.package = package
            booking.save()
            sweetify.success(request,'Booking Submit Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('gym_web_index')
    else:
        form = BookingForm()
    return render(request, 'web_booking.html', {'form': form, 'package': package, 'shifts': shifts})

@login_required(login_url='/login/')
def user_bookings(request):
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user)
        return render(request, 'booking_history.html', {'user_bookings': user_bookings})
    
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    sweetify.success(request,'Delete Sucessfull', timer=5000, timerProgressBar='true', persistent="Close")
    return redirect('booking_detail')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    packages = MembershipPackage.objects.all()
    shifts = Shifts.objects.all()
    if request.method == 'POST':
        form = BookingEditForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Edit Sucessfull', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('booking_detail')  # Redirect to the booking detail page
    else:
        form = BookingEditForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form,'packages':packages,'shifts':shifts})