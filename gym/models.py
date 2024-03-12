from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    joindate = models.DateField(max_length=40)
    expiredate = models.DateField(max_length=40)
    initialamount = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    
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
