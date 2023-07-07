from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category' , views.CategoryViewset , basename="category")
router.register('policy' , views.PolicyViewSet , basename='policy')
router.register('policy-choose' , views.PolicyRecordViewset , basename='policy_choose')

urlpatterns = router.urls