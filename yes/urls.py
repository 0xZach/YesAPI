from django.urls import path, include
from django.contrib.auth.models import Group,  User
from rest_framework import routers, serializers, viewsets

#from . import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# urls inside the app
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


""" EXAMPLES
    # when using a class, need to call the as_view method as we don't use a simple view function
    path("", views.Index, name="index"), 
    path("ascent_details/<int:pk>/", views.AscentDetailsView.as_view(), name="ascent-details"),
    path("<int:pk>/delete/",views.AscentDeleteView.as_view(), name="ascent-delete"),
    path("list/", views.ascent_list, name="list"),
    path("upload/", views.upload_ascent, name="upload-ascent"),

"""