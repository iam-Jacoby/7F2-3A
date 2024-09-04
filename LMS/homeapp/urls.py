from django.urls import path
from homeapp.views import signup_view, signin_view, logout_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('logout/', logout_view, name='logout'),
]