from rest_framework import viewsets
from rest_framework import mixins

from .models import Advice, Review, Teacher
from .serializers import AdviceSerializer, ReviewReadSerializer, ReviewWriteSerializer, TeacherSerializer
from .filters import TeacherFilterSet, ReviewFilterSet


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Получение/добавление отзывов."""
    queryset = Review.objects.all()
    filterset_class = ReviewFilterSet
    search_fields = ('^teacherOrCourse',)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewWriteSerializer
        return ReviewReadSerializer


class AdviceViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Получение/добавление советов."""
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class TeacherViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Получение списка учителей"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilterSet
    search_fields = ('^name',)
