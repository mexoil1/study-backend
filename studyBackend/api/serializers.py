from rest_framework import serializers

from .models import Advice, Review, Teacher


class ReviewReadSerializer(serializers.ModelSerializer):
    """Cериалайзер чтения отзывов."""
    teacher = serializers.ReadOnlyField(source='teacherOrCourse.name')

    class Meta:
        model = Review
        fields = ('course', 'teacher', 'text')


class ReviewWriteSerializer(serializers.ModelSerializer):
    """Cериалайзер написания отзывов."""

    class Meta:
        model = Review
        fields = '__all__'


class AdviceSerializer(serializers.ModelSerializer):
    """Сериалайзер советов."""

    class Meta:
        model = Advice
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    """Сериалайзер Учителей или курсов."""

    class Meta:
        model = Teacher
        fields = '__all__'
