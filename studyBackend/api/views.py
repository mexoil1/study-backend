from rest_framework import viewsets
from rest_framework import mixins

from .models import Advice, FAQ, Review, Teacher
from .serializers import AdviceSerializer, FAQSerializer, ReviewSerializer, TeacherSerializer


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Получение/добавление отзывов."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AdviceViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Получение/добавление советов."""
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class FAQViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """FAQ"""
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class TeacherViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Получение списка учителей"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
