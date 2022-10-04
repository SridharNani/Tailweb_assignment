
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.



class UserProfile(AbstractUser):
    username = models.CharField(max_length=200,null=True)
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    # def __init__(self):
    #     return  self.username


class Student(models.Model):
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
    Name = models.CharField(max_length=50)
    Subject = models.CharField(max_length=50)
    Marks = models.IntegerField(blank=True,null=True)









# Companies
# Samsung
# Apple
# LG



#
# Category
# Mobile
# Refrigerator
# Television

# class category(models.Model):
#     c_name=models.CharField(max_length=100)
#     # Refrigerator=models.CharField(max_length=100)
#     # Television=models.CharField(max_length=100)
#
#
# class companies(models.Model):
#     company_name=models.CharField(max_length=100)
#
#
# class product(models.Model):
#     name=models.ManyToManyField(on_delete=models.CASCADE,companies)
# # class category(models.Model):










