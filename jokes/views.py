from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JokeSerializer
from .models import Joke


class JokeViewSet(viewsets.ModelViewSet):
    serializer_class = JokeSerializer
    queryset = Joke.objects.all()
