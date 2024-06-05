from rest_framework import serializers
from .models import UserFoodLog, CalorieRequirement, UserFoodRecommendation

class UserFoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodLog
        fields = '__all__'

class CalorieRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieRequirement
        fields = '__all__'

class UserFoodRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodRecommendation
        fields = '__all__'
