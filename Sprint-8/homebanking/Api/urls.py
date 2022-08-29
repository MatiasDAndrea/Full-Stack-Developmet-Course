from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('Cliente',views.ClienteView,basename="Cliente")
router.register('Cuentas',views.CuentaView,basename="Cuenta")
router.register('Prestamos',views.PrestamosView,basename="Prestamos")
router.register('PrestamosAdmin',views.PrestamoEmpleado,basename="PrestamosEmpleados")
router.register('Tarjetas',views.TarjetasView,basename="Tarjetas")
router.register('Direccion',views.DirectionsView,basename="Direcciones")

urlpatterns = router.urls