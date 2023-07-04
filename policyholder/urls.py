from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category' , views.CategoryViewset , basename="category")


urlpatterns = router.urls