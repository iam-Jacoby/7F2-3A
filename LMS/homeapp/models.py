from django.contrib.auth.models import AbstractUser
from django.db import models

# Define your custom user model by extending AbstractUser
class User(AbstractUser):
    account_type = [
        ("AD", "Admin"),
        ("ST", "Student"),
        ("IN", "Instructor"),
    ]
    
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=60)
    user_type = models.CharField(max_length=2, choices=account_type)
    # Other custom fields can be added here

    def __str__(self):
        return self.username

# from django.db import models

# # Create your models here.
# class User(models.Model):
#     account_type = [
#         ("AD", "Admin"),
#         ("ST", "Student"),
#         ("IN", "Instructor"),
#     ]
#     user_id = models.BigAutoField(primary_key=True)
#     email = models.EmailField(max_length=254)
#     name = models.CharField(max_length=60)
#     user_type = models.CharField(max_length=2, choices=account_type)
