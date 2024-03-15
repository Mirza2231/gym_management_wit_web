from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import *
from .forms import *
import sweetify
from django.views.generic import DetailView

# Create your views here.


def Home(request):
   return render(request, 'admin_index.html')
 
def About(request):
    return render(request, 'about.html')

# My Work Start

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

def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('add_trainer')

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


def delete_pcategory(request, pcategory_id):
    pcategory = PCategory.objects.get(id=pcategory_id)
    pcategory.delete()
    return redirect('add_pcategory')

class PcategoryDetailView(DetailView):
    model = PCategory
    template_name = 'pcategory_detail.html'  # The template to render
    context_object_name = 'pcategory'
    
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
    
def delete_package(request, package_id):
    package = MembershipPackage.objects.get(id=package_id)
    package.delete()
    return redirect('add_package')


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

def adminLogout(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    logout(request)
    return redirect('adminlogin')

# My Work End

def Table(request):
    return render(request, 'basic-table.html')








def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(
                name=n, contact=c, emailid=e, age=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)
def Delete_Enquiry(request,pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        try:
            Equipment.objects.create( name=n, price=p, unit=u, date=d, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'view_equipment.html', d)

def Delete_Equipment(request,pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create( name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        try:
            Member.objects.create( name=n, contact=c,emailid=e, age=a,gender=g,plan=plan, joindate=joindate, expiredate = expiredate, initialamount = initialamount)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'plan':plan1}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request,pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')
