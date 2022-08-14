from django.contrib import admin
from django.urls import path, include
from Prestamos import views


urlpatterns = [
    path('Prestamos',views.PrestamoPackage.log_page,name="prestamos"),
    path('Prestamos/Mensaje/',views.PrestamoPackage.mensaje)
]