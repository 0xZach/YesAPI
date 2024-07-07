from django.contrib import admin
from .separate_models.Country import Country
from .separate_models.Person import Person
from .separate_models.CustomUser import CustomUser
#from .separate_models.User import User


admin.site.register(CustomUser)
admin.site.register(Country)
admin.site.register(Person)