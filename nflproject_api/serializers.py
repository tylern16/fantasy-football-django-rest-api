from rest_framework import serializers 
from .models import Team 

class TeamSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Team # tell django which model to use
        fields = ('id', 'name', 'players',) # tell django which fields to include
