from rest_framework import serializers

from .models import Advice, Review


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
