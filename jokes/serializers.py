from .models import Joke
from rest_framework import serializers


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ('title', 'content')