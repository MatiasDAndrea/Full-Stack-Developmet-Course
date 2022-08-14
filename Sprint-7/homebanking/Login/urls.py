from django.contrib import admin
from django.urls import path
from Login import views


urlpatterns = [
    path('',views.LoginPackage.home,name="home"),
]