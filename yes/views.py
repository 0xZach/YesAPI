from django.shortcuts import get_object_or_404

from .separate_models.CustomModelViewSet import CustomModelViewSet

from .separate_models.Person import Person
from .separate_models.Country import Country

from .serializers import (PeopleSerializer,CountriesSerializer)



# this is the most basic a view can get
class CountriesViewSet(CustomModelViewSet):
    
    # Attributes
    
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
    
    
    # Methods




class PeopleViewSet(CustomModelViewSet):
    
    # Attributes
    
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    
    
    # Methods