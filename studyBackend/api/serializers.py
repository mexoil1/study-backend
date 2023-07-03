from rest_framework import serializers

from .models import Advice, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        
        
class AdviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Advice
        fields = '__all__'
