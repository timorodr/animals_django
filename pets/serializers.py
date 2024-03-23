from .models import Turtle
from rest_framework import serializers

class TurtleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Turtle
        fields='__all__'