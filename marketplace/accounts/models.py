from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    USER_TYPES = [
        ('jobseeker', 'Job Seeker'),
        ('employer', 'Employer'),
        ('contractor', 'Contractor'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
