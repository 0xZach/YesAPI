from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/', include(('yes.urls','yes'),namespace='yes_app')), #namespaces are weird, dude
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]