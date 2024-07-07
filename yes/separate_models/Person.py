from django.db import models
from .Country import Country


class Person(models.Model):
    
    # Attributs
    
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=16)
    home_country = models.ForeignKey(Country, default=0, related_name='FK_homeC', on_delete=models.CASCADE)
    host_country = models.ForeignKey(Country, default=0, related_name='FK_hostC', on_delete=models.CASCADE)


    # Methods
   
    def __str__(self):
        return (
            "-- Person --\n name: " + self.name 
            + "\nage: " + str(self.age)
            + "\nhome country: " + self.home_country.name
            + "\nhost country: " + self.host_country.name
            + "\n--------"
        )