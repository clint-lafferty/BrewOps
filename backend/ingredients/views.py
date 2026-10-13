from django.shortcuts import render
from rest_framework import generics
from .models import Ingredient
from .serializers import IngredientSerializer

# Create your views here.
class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer