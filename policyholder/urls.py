from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('category', views.CategoryViewset, basename="category")
router.register('policy', views.PolicyViewSet, basename='policy')
router.register('policy-choose', views.PolicyRecordViewset,
                basename='policy_record')
router.register('question', views.QuestionViewset, basename='question')


urlpatterns = router.urls
urlpatterns += [
    path('policy_detail/<int:pk>/',
         views.PolicyDetailView.as_view(), name='PolicyDetailView')
]
