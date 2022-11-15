from rest_framework import serializers
from .models import Game

from user.serializer import UserSerializer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['owner'] = UserSerializer(instance.owner).data
        return response
