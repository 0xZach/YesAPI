from rest_framework import serializers

from .separate_models.Person import Person
from .separate_models.Country import Country


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','name','flag_link']

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'home_country','host_country']