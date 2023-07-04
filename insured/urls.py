from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('insurer' , views.InsurerViewSet , basename="insurer")

urlpatterns = router.urls