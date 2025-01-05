from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=5, null=True, default=None)
    
    def __str__(self):
        return self.name
    
class Itinerary(models.Model):
    id = models.CharField(max_length=10, default=None, primary_key=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    legs = models.ManyToManyField('Leg', related_name='legs')
    def __str__(self):
        return f"{self.agent} - {self.agent_rating} - {self.price}"

class Leg(models.Model):
    id = models.CharField(max_length=5, default=None, primary_key=True)
    departure_airport = models.CharField(max_length=3)
    arrival_airport = models.CharField(max_length=3)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    duration_mins = models.IntegerField()
    
    def __str__(self):
        return f"{self.airline_name} - {self.departure_airport} To {self.arrival_airport} "


