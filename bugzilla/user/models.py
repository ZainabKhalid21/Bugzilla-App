from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    User_types = (
        ('d', 'Developer'),
        ('m', 'Manager'),
        ('q', 'QA'),
    )
    
    user_email=models.EmailField(max_length=100)
    user_type = models.CharField(max_length=1, choices=User_types)
    