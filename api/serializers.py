from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.Serializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description')

class RatingSerializer(serializers.Serializer):
    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')