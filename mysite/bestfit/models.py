from django.db import models
from django.contrib.auth.models import User


subjects = (("Eng", "English"), ("datastruct", "Datastructure"), ("Programing", "Programming"), ("Comp", "Computer"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f' {self.user.username} Profile'


class Registerations(models.Model):
    education_choices = (("Matric", "Matric"), ("Intermediate", "Intermediate"),("Diploma", "Diploma"), ("Master", "Master"), ("PHD", "PHD"))
    first_name = models.TextField(max_length=50, blank=True)
    last_name = models.TextField(max_length=50, blank=True)
    mobile = models.CharField(max_length=14, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    education = models.CharField(max_length=100, choices=education_choices)
    def __str__(self):
        return self.first_name


class ProfileEdit(models.Model):
    registerations_form = models.ForeignKey(Registerations, on_delete=models.CASCADE, default='')
    gender_choice = (("Male", "Male"), ("Female", "Female"))
    DOB = models.DateField(blank=True, null=True)
    address_1 = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choice)
    interest = models.CharField(max_length=120, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)

