from django.db import models
from .managers import CustomizeUserManager
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    USER_CHOICES = [
        ('SELECT_CHOICE', ''),
        ('admin','Admin'),
        ('pharmacist','Pharmacist'),
        ('supplier','Supplier')
    ]
    
    user_type = models.CharField(max_length=255,choices=USER_CHOICES,verbose_name="User Type")
    email = models.EmailField(max_length=255,verbose_name="Email address",unique=True)
    username = None
    first_name = None
    last_name = None
    
    object = CustomizeUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[ 'user_type',]
    
    def __str__(self):
        return self.email
    
