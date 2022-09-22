from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Student(models.Model):
    Name = models.CharField(max_length=50)
    Subject = models.CharField(max_length=50)
    Marks = models.IntegerField(blank=True,null=True)



