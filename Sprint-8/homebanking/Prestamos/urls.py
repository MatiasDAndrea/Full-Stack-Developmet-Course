from django.contrib import admin
from django.urls import path, include
from Prestamos import views
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('API_Prestamos',views.PrestamosView,basename="API_Prestamos")
router.register('API_PrestamosAdmin',views.PrestamoEmpleado,basename="API_PrestamosAdmin")
urlpatterns = router.urls

urlpatterns += [
    path('Prestamos',views.PrestamoPackage.log_page,name="prestamos"),
    path('Prestamos/Mensaje/',views.PrestamoPackage.mensaje)

]