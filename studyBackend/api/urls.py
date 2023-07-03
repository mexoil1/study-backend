from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import ReviewViewSet, AdviceViewSet

app_name = 'api'
router = DefaultRouter()
router.register('reviews', ReviewViewSet)
router.register('advices', AdviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]