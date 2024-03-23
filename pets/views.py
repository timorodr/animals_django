from django.shortcuts import render
from .models import Turtle
from rest_framework import viewsets, permissions
from .serializers import TurtleSerializer
# Create your views here.
class TurtleViewSet(viewsets.ModelViewSet):
    queryset=Turtle.objects.all().order_by('id') # order by id is optional

    serializer_class=TurtleSerializer

    permission_classes=[permissions.AllowAny]