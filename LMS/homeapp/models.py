from django.db import models
from django.contrib.auth.models import User

class User_types(models.Model):
    USER_TYPE_CHOICES = [
        ('STU', 'Student'),
        ('INS', 'Instructor'),
        ('ADM', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES)