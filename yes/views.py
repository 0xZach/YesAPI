from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

from .separate_models.Person import Person
from .separate_models.Country import Country

from .serializers import (PeopleSerializer,CountriesSerializer)

class PeopleViewSet(viewsets.ModelViewSet):
    # Allows only authenticated users
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Person.objects.all()
    serializer_class = PeopleSerializer

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer