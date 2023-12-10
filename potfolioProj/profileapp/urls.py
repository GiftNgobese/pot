from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('sponsor-signin/', views.sponsorSignin, name='sponsor-signin'),
    # path('sponsor-signup/', views.sponsorSignup, name='sponsor-signup'),
    
]