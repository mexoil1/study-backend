from django_filters.rest_framework import FilterSet, filters

from .models import Teacher, Review


class TeacherFilterSet(FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Teacher
        fields = ['name']


class ReviewFilterSet(FilterSet):
    teacherOrCourse__name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Review
        fields = ['teacherOrCourse__name']
