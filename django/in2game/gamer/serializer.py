from rest_framework import serializers
from .models import Gamer


class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('__all__')
