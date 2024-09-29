from django.urls import path
from . import views
from .views import UserRegistrationView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]
