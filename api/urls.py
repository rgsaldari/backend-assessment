from django.urls import path
from api import views


urlpatterns = [
    # Agent routes
    path('agents/', views.agent_list, name='agent_list'),
    path('agent/<int:id>/', views.agent_detail, name='agent_detail'),

    # Airline routes
    path('airlines/', views.airline_list, name='airline_list'),
    path('airline/<int:id>/', views.airline_detail, name='airline_detail'),

    # Leg routes
    path('legs/', views.leg_list, name='leg_list'),
    path('leg/<int:id>/', views.leg_detail, name='leg_detail'),

    # Itinerary routes
    path('itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itinerary/<int:id>/', views.itinerary_detail, name='itinerary_detail'),
]