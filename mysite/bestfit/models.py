from django.db import models
from django.contrib.auth.models import User

subjects = (("Eng","English"),("datastruct","Datastructure"),("Programing","Programming"),("Comp","Computer"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f' {self.user.username} Profile'


class Test(models.Model):
    category = models.CharField(max_length=64, choices=subjects,default=None)
    question = models.CharField(max_length=255)
    A = models.CharField(max_length=255)
    B = models.CharField(max_length=255)
    C = models.CharField(max_length=255)
    D = models.CharField(max_length=255)
    answer_correct = models.CharField(max_length=255, default=None)
