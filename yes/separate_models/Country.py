from django.db import models

class Country(models.Model):

    # Attributs
    id = models.CharField(primary_key=True,max_length=2,unique=True) # based on the 2 letters code
    name = models.CharField(max_length=100)
    flag_link = models.CharField(max_length=100) # remembering the name attributed to the static image of the flag


    # Methods

    def __str__(self):
        return (
            "-- Country --\n id: " + self.id 
            + "\nname: " + self.name 
            + "\nflag link: " + self.flag_link
            + "\n--------"
        )