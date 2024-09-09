from django.urls import path
from . import views

urlpatterns = [
    # path('', views.temporary, name='temporary'),    # Added From Friend's Code

    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
]