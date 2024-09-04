from django.db import models
from django.contrib.auth.models import AbstractUser

# <<<<<<< HEAD
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
# =======
# Create your models here.
class User(models.Model):
    account_type = [
        ("AD", "Admin"),
        ("ST", "Student"),
        ("IN", "Instructor"),
    ]
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=60)
    user_type = models.CharField(max_length=2, choices=account_type)
# >>>>>>> 8f7359756ad0548684e10e0a8afd409cd4413146
