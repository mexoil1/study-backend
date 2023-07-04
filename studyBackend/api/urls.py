from rest_framework.routers import DefaultRouter
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from .views import ReviewViewSet, AdviceViewSet

app_name = 'api'
router = DefaultRouter()
router.register('reviews', ReviewViewSet)
router.register('advices', AdviceViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), 


]