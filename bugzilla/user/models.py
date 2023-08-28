from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    User_types = (
        ('d', 'Developer'),
        ('m', 'Manager'),
        ('q', 'QA'),
    )
    # user_name=models.CharField(max_length=100)
    # user_id=models.IntegerField(unique=True)
    # user_password=models.CharField(max_length=10)
    user_email=models.EmailField(max_length=100)
    user_type = models.CharField(max_length=1, choices=User_types)
    