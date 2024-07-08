from rest_framework.routers import DefaultRouter
from yes.views import PeopleViewSet,CountriesViewSet

# The router method helps define the different urls that are gonna be used
router = DefaultRouter()
router.register(r'People', PeopleViewSet, basename="people")
router.register(r'Countries', CountriesViewSet, basename="countries")

urlpatterns = router.urls