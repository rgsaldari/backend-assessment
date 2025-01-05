from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Agent,Airline,Itinerary,Leg
from .serializers import AgentSerializer,AirlineSerializer,ItinerarySerializer,LegSerializer

# Create your views here.



# List all Agents (GET request)
@api_view(['GET'])
def agent_list(request):
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)


# Retrieve a single Agent (GET request by ID)
@api_view(['GET'])
def agent_detail(request, id):
    try:
        agent = Agent.objects.get(pk=id)
    except Agent.DoesNotExist:
        return Response({'error': 'Agent not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AgentSerializer(agent)
        return Response(serializer.data)


# List all Airlines (GET request)
@api_view(['GET'])
def airline_list(request):
    if request.method == 'GET':
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data)


# Retrieve a single Airline (GET request by ID)
@api_view(['GET'])
def airline_detail(request, id):
    try:
        airline = Airline.objects.get(pk=id)
    except Airline.DoesNotExist:
        return Response({'error': 'Airline not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AirlineSerializer(airline)
        return Response(serializer.data)


# Retrieve a single Leg (GET request by ID)
@api_view(['GET'])
def leg_detail(request, id):
    try:
        leg = Leg.objects.get(pk=id)
    except Leg.DoesNotExist:
        return Response({'error': 'Leg not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LegSerializer(leg)
        return Response(serializer.data)


# Leg List
@api_view(['GET'])
def leg_list(request):
    legs = Leg.objects.all()
    serializer = LegSerializer(legs, many=True)
    return Response(serializer.data)


# Retrieve a single Itinerary (GET request by ID)
@api_view(['GET'])
def itinerary_detail(request, id):
    try:
        itinerary = Itinerary.objects.get(pk=id)
    except Itinerary.DoesNotExist:
        return Response({'error': 'Itinerary not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data)

# Itinerary List
@api_view(['GET'])
def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    serializer = ItinerarySerializer(itineraries, many=True)
    return Response(serializer.data)


    

