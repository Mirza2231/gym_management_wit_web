from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Trainer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12,unique=True)
    email = models.CharField(max_length=50,unique=True)
    age = models.IntegerField(max_length=40)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    instalink = models.CharField(max_length=500)
    xlink = models.CharField(max_length=400)
    facebooklink = models.CharField(max_length=400)
    profile_pic = models.ImageField(upload_to='trainer_pics', blank=True)


    def __str__(self):
        return self.name

class PCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class MembershipPackage(models.Model):
    package_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(PCategory, on_delete=models.CASCADE)
    facilities = models.TextField()

    def __str__(self):
        return self.package_name
    
    
class Shifts(models.Model):
    shift = models.CharField(max_length=100)

    def __str__(self):
        return self.shift
    
