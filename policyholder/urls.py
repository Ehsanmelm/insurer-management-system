from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category' , views.CategoryViewset , basename="category")
router.register('policy' , views.PolicyViewSet , basename='policy')

urlpatterns = router.urls