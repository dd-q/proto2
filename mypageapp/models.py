from django.db import models
from django.db.models.fields import *

class User(models.Model):
    user_name = CharField(max_length=50)
    email = CharField(max_length=100)
    user_phone = CharField(max_length=11)
    user_addr = CharField(max_length=250)
    profile_img = models.FileField(upload_to='%Y%m%d', null=True, blank = True)
    def __str__(self):
        return self.user_name


class Pet(models.Model):
    pet_name = CharField(max_length=50, null=True, blank=True)
    gender = CharField(max_length=1, null=True, blank=True)
    age = DateField(null=True, blank=True)
    size = CharField(max_length=1, null=True, blank=True)
    neutered = CharField(max_length=1, null=True, blank=True)
    pet_img = models.ImageField(upload_to='%Y%m%d', null=True, blank = True)
    # user = models.ForeignKey(User, unique=True, on_delete = models.CASCADE, null = True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.pet_name


