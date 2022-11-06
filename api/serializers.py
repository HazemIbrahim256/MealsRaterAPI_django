from rest_framework import serializers
from .models import Meal, Rating

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description', 'num_of_ratings', 'avg_rate')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')
