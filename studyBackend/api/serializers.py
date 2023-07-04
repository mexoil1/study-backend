from rest_framework import serializers

from .models import Advice, FAQ, Review, Teacher


class ReviewSerializer(serializers.ModelSerializer):
    """Cериалайзер отзывов."""
    
    class Meta:
        model = Review
        fields = '__all__'
        
        
class AdviceSerializer(serializers.ModelSerializer):
    """Сериалайзер советов."""
    
    class Meta:
        model = Advice
        fields = '__all__'
        
        
class FAQSerializer(serializers.ModelSerializer):
    """Сериалайзер FAQ."""
    
    class Meta:
        model = FAQ
        fields = '__all__'
        
        
class TeacherSerializer(serializers.ModelSerializer):
    """Сериалайзер Учителей или курсов."""
    
    class Meta:
        model = Teacher
        fields = '__all__'
