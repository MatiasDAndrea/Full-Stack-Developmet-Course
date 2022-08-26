from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('Cliente',views.ClienteView,basename="Cliente")
router.register('Cuenta',views.CuentaView,basename="Cuenta")

urlpatterns = router.urls