from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
