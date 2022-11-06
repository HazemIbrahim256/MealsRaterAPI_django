from django.shortcuts import render
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods = ["POST"], detail = True)
    def rate_meal(self, request, pk = None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = Meal.objects.get(id = pk)
            username = request.data['username']
            stars = request.data['stars']

            user = User.objects.get(username = username)
            try:
                #update 
                rate = Rating.objects.get(user=user.id, meal = meal.id)
                rate.stars = stars
                rate.save()
                serializer = RatingSerializer(rate, many=False)
                json = {
                    'message' : 'Meal rate updated',
                    'result' : serializer.data
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
            except:
                #create
                rate = Rating.objects.create(stars = stars, meal = meal,user = user)
                serializer = RatingSerializer(rate, many=False)
                json = {
                    'message' : 'Meal rate created',
                    'result' : serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            json = {
                'message' : 'Stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
