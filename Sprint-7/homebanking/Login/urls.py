from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.LoginPackage.login,name="Login"),
    path('message/',views.LoginPackage.login_action,name="Login_action"),
]