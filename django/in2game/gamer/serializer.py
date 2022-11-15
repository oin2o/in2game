from rest_framework import serializers
from .models import Gamer

from game.serializer import GameSerializer
from user.serializer import UserSerializer


class GamerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gamer
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['game'] = GameSerializer(instance.game).data
        response['user'] = UserSerializer(instance.user).data
        return response
