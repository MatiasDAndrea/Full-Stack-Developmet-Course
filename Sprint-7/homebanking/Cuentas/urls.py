from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.CuentasPackage.cuenta,name="cuenta"),
    path('goCripto',views.CuentasPackage.gocripto_render,name="gocripto")
]