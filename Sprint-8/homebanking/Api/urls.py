from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('Cliente',views.ClienteView,basename="Cliente")
router.register('Cuentas',views.CuentaView,basename="Cuenta")
router.register('Prestamos',views.PrestamosView,basename="Cuenta")

urlpatterns = router.urls