# flights/tasks.py

import requests
from datetime import datetime
from celery import shared_task
from .models import Agent, Airline, Itinerary, Leg

@shared_task
def import_flights_data_from_url():
    url = 'https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json'

    try:    
        # Fetch data from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)
        
        # Parse JSON data
        data = response.json()

        # Create a list to store created agents and airlines to avoid duplicates
        agents = {}
        airlines = {}

        # Create airlines
        for leg in data["legs"]:
            airline = (leg["airline_name"], leg["airline_id"])
            if airline not in airlines:
                airlines[airline] = None
                
        for (airline_name, airline_id), _ in airlines.items(): 
            Airline.objects.get_or_create(
            short=airline_id,
            name=airline_name
    )


        # Create agents
        for itinerary in data["itineraries"]:
            agent = (itinerary["agent"], itinerary["agent_rating"])
            if agent not in agents:
                agents[agent] = None
                
        for (agent_name, agent_rating), _ in agents.items():
            Agent.objects.get_or_create(
                rating=agent_rating,
                name=agent_name
            )

        # Create legs
        for leg_data in data["legs"]:
            leg_id = leg_data["id"]
            leg_departure_airport = leg_data["departure_airport"]
            leg_arrival_airport = leg_data["arrival_airport"]
            leg_dep_time = leg_data["departure_time"]
            leg_arr_time = leg_data["arrival_time"]
            leg_stops = leg_data["stops"]
            leg_airline_id = leg_data["airline_id"]
            leg_duration_mins = leg_data["duration_mins"]
            
            leg_airline = Airline.objects.get(short=leg_airline_id)
        
            Leg.objects.get_or_create(
                id=leg_id,
                departure_airport=leg_departure_airport,
                arrival_airport=leg_arrival_airport,
                departure_time=leg_dep_time,
                arrival_time=leg_arr_time,
                stops=leg_stops,
                airline=leg_airline,
                duration_mins=leg_duration_mins,
            )
        
        # Create itineraries
        for itinerary_data in data["itineraries"]:
            itinerary_id = itinerary_data["id"]
            itinerary_legs = itinerary_data["legs"]
            itinerary_price = itinerary_data["price"]
            itinerary_agent_name = itinerary_data["agent"]
            
            legs = Leg.objects.filter(id__in=itinerary_legs)
            
            itinerary_agent = Agent.objects.get(name=itinerary_agent_name)
            
            itinerary, created = Itinerary.objects.get_or_create(
                id=itinerary_id,
                defaults={
                    "price": float(itinerary_price[1:]),  # Assuming price has a currency symbol
                    "agent": itinerary_agent,
                }
            )
            itinerary.legs.set(legs)
        
        return 'Data import successful'
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    except Exception as e:
        return f"An error occurred during import: {e}"
