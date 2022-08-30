from Prestamos import views
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('API_Tarjetas',views.TarjetasView,basename="API_Tarjetas")
urlpatterns = router.urls