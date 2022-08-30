from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('API_Cliente',views.ClienteView,basename="API_Cliente")
router.register('API_Direcciones',views.DirectionsView,basename="API_Direcciones")
router.register('API_Sucursales',views.SucursalesView,basename="API_Sucursales")

urlpatterns = router.urls