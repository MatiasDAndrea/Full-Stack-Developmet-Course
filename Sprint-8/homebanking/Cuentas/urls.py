from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('API_Cuenta',views.CuentaView,basename="API_Cuenta")
urlpatterns = router.urls

urlpatterns += [
    path('',views.CuentasPackage.cuenta,name="cuenta"),
    path('goCripto',views.CuentasPackage.gocripto_render,name="gocripto")
]