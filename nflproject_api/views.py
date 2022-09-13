from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import TeamSerializer
from .models import Team

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TeamSerializer # tell django what serializer to use

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer
