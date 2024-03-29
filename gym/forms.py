from django import forms
from .models import *
from gym_web.models import *

class AddTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'contact', 'email', 'age','gender','instalink','xlink','facebooklink','profile_pic']
        
class TrainerEditForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'contact', 'email', 'age','gender','instalink','xlink','facebooklink','profile_pic'] 
        
class PcategoryForm(forms.ModelForm):
    class Meta:
        model = PCategory
        fields = ['name', 'description'] 
        
class PcategoryEditForm(forms.ModelForm):
    class Meta:
        model = PCategory
        fields = ['name', 'description'] 

class MembershipPackageForm(forms.ModelForm):
    class Meta:
        model = MembershipPackage
        fields = ['package_name', 'price', 'category', 'facilities']

    def clean_facilities(self):
        facilities = self.cleaned_data['facilities']
        # Split input by commas, strip whitespace from each facility,
        # and remove empty elements caused by consecutive commas
        facilities = [facility.strip() for facility in facilities.split(',') if facility.strip()]
        return ','.join(facilities)  # Join back into a comma-separated
    
class PackageEditForm(forms.ModelForm):
    class Meta:
        model = MembershipPackage
        fields = ['package_name', 'price', 'category', 'facilities']

    def clean_facilities(self):
        facilities = self.cleaned_data['facilities']
        # Split input by commas, strip whitespace from each facility,
        # and remove empty elements caused by consecutive commas
        facilities = [facility.strip() for facility in facilities.split(',') if facility.strip()]
        return ','.join(facilities)  # Join back into a comma-separated
    
class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shifts
        fields = ['shift'] 
        
class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']