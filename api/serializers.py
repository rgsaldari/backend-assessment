from rest_framework import serializers
from .models import Agent,Airline,Itinerary,Leg

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name','rating']
        
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name','short']
        
class LegSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    class Meta:
        model = Leg
        fields = '__all__' 
        
        
class ItinerarySerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    legs = LegSerializer(many=True)

    class Meta:
        model = Itinerary
        fields = '__all__'