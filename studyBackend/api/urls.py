from rest_framework.routers import DefaultRouter
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from .views import AdviceViewSet, FAQViewSet, ReviewViewSet, TeacherViewSet

app_name = 'api'
router = DefaultRouter()
router.register('reviews', ReviewViewSet)
router.register('advices', AdviceViewSet)
router.register('faq', FAQViewSet)
router.register('teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]