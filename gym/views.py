from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *
from gym_web.models import *
from .forms import *
import sweetify
from django.views.generic import DetailView

# Create your views here.
 
def About(request):
    return render(request, 'about.html')

# My Work Start

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'booking'

@login_required(login_url='/admin_login/')
def all_bookings(request):
    # Query all bookings
    all_bookings = Booking.objects.all()

    context = {
        'all_bookings': all_bookings,
    }
    return render(request, 'admin_booking.html', context)

@login_required(login_url='/admin_login/')
def edit_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    current_status = booking.status  # Get the current status of the booking

    if request.method == 'POST':
        new_status = request.POST.get('status')
        booking.status = new_status
        booking.save()
        return redirect('admin_booking')

    return render(request, 'edit_booking_status.html', {'booking': booking, 'current_status': current_status})

@login_required(login_url='/admin_login/')
def Home(request):
    users = User.objects.filter(is_staff=False)  # Query data from Model1
    trainers = Trainer.objects.all()  # Query data from Model1
    pcategorys = PCategory.objects.all()  # Query data from Model2
    packges = MembershipPackage.objects.all()  # Query data from Model3
    shifts = Shifts.objects.all()  # Query data from Model3
    
    # Add more queries for other models as needed

    context = {
        'trainers': trainers,
        'pcategorys': pcategorys,
        'packges': packges,
        'shifts': shifts,
        'users': users,
        
        
        # Add more data as needed
    }
    return render(request, 'admin_index.html', context)

@login_required(login_url='/admin_login/')
def ad_tariner(request):
    trainers = Trainer.objects.all()
    if request.method == 'POST':
        trainer_form = AddTrainerForm(request.POST, request.FILES)
        if trainer_form.is_valid():
            trainer_form.save()
            sweetify.success(request, 'Your Submission Has Done Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
        else:
            sweetify.error(request, 'Something Wrong Try Again Later', timer=5000, timerProgressBar='true', persistent="Close")

    else:
        trainer_form = AddTrainerForm()
    return render(request, 'admin_trainers.html', {'trainer_form': trainer_form, 'trainers': trainers})

@login_required(login_url='/admin_login/')
def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('add_trainer')

@login_required(login_url='/admin_login/')
def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        et_form = TrainerEditForm(request.POST, request.FILES, instance=trainer)
        if et_form.is_valid():
            et_form.save()
            sweetify.success(request, 'Trainer Edited Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('add_trainer')  # Redirect to the list of trainers after editing
        else:
            sweetify.error(request, 'Some Error Occured', timer=5000, timerProgressBar='true', persistent="Close")
            
    else:
        et_form = TrainerEditForm(instance=trainer)
    return render(request, 'edit_trainer.html', {'et_form': et_form})

class TrainerDetailView(DetailView):
    model = Trainer
    template_name = 'trainer_detail.html'  # The template to render
    context_object_name = 'trainer'
    
@login_required(login_url='/admin_login/')
def pcategory(request):
    pcategorys = PCategory.objects.all()
    if request.method == 'POST':
        pcategory_form = PcategoryForm(request.POST)
        if pcategory_form.is_valid():
            pcategory_form.save()
            sweetify.success(request, 'Your Submission Has Done Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
        else:
            sweetify.error(request, 'Something Wrong Try Again Later', timer=5000, timerProgressBar='true', persistent="Close")

    else:
        pcategory_form = PcategoryForm()
    return render(request, 'admin_pcategory.html', {'pcategory_form': pcategory_form, 'pcategorys': pcategorys})

@login_required(login_url='/admin_login/')
def edit_pcategory(request, pcategory_id):
    pcategory = get_object_or_404(PCategory, id=pcategory_id)
    if request.method == 'POST':
        etpc_form = PcategoryEditForm(request.POST, request.FILES, instance=pcategory)
        if etpc_form.is_valid():
            etpc_form.save()
            sweetify.success(request, 'Category Edited Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('add_pcategory')  # Redirect to the list of trainers after editing
        else:
            sweetify.error(request, 'Some Error Occured', timer=5000, timerProgressBar='true', persistent="Close")
            
    else:
        etpc_form = PcategoryEditForm(instance=pcategory)
    return render(request, 'edit_pcategory.html', {'etpc_form': etpc_form})

@login_required(login_url='/admin_login/')
def delete_pcategory(request, pcategory_id):
    pcategory = PCategory.objects.get(id=pcategory_id)
    pcategory.delete()
    return redirect('add_pcategory')

class PcategoryDetailView(DetailView):
    model = PCategory
    template_name = 'pcategory_detail.html'
    context_object_name = 'pcategory'
    
@login_required(login_url='/admin_login/')
def membership_package(request):
    packages = MembershipPackage.objects.all() 
    categories = PCategory.objects.all()
    if request.method == 'POST':
        form = MembershipPackageForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Your Submission Has Done Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('add_package')
        else:
            sweetify.error(request, 'Something Wrong Try Again Later', timer=5000, timerProgressBar='true', persistent="Close")
    else:
        form = MembershipPackageForm()
    return render(request, 'admin_package.html', {'form': form, 'packages': packages,'categories':categories})

@login_required(login_url='/admin_login/')
def edit_package(request, package_id):
    package = get_object_or_404(MembershipPackage, id=package_id)
    s_category = PCategory.objects.all() 
    if request.method == 'POST':
        etp_form = PackageEditForm(request.POST, request.FILES, instance=package)
        if etp_form.is_valid():
            etp_form.save()
            sweetify.success(request, 'Package Edited Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
            return redirect('add_package')  # Redirect to the list of trainers after editing
        else:
            sweetify.error(request, 'Some Error Occured', timer=5000, timerProgressBar='true', persistent="Close")
            
    else:
        etp_form = PackageEditForm(instance=package)
    return render(request, 'edit_package.html', {'etp_form': etp_form, 's_category':s_category})

class PackageDetailView(DetailView):
    model = MembershipPackage
    template_name = 'package_detail.html'  # The template to render
    context_object_name = 'package'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package = self.object  # Get the current MembershipPackage object
        category = package.category  # Get the related category object
        context['category'] = category  # Add the category object to the context
        return context
    
@login_required(login_url='/admin_login/')
def delete_package(request, package_id):
    package = MembershipPackage.objects.get(id=package_id)
    package.delete()
    return redirect('add_package')

@login_required(login_url='/admin_login/')
def add_shift(request):
    shifts = Shifts.objects.all()
    if request.method == 'POST':
        shift_form = ShiftForm(request.POST)
        if shift_form.is_valid():
            shift_form.save()
            sweetify.success(request, 'Your Submission Has Done Sucessfully', timer=5000, timerProgressBar='true', persistent="Close")
        else:
            sweetify.error(request, 'Something Wrong Try Again Later', timer=5000, timerProgressBar='true', persistent="Close")

    else:
        shift_form = ShiftForm()
    return render(request, 'add_shift.html', {'shift_form': shift_form, 'shifts':shifts})

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                return redirect('add_package') 
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'adminlogin.html', d)

@login_required(login_url='/admin_login/')
def adminLogout(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    logout(request)
    return redirect('adminlogin')

# My Work End