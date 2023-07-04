from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import Advice, Review
from .serializers import AdviceSerializer, ReviewSerializer

@extend_schema()
class ReviewViewSet(viewsets.ModelViewSet):
    """Получение/добавление отзывов."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class AdviceViewSet(viewsets.ModelViewSet):
    """Получение/добавление советов."""
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
