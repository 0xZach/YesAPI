from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated


"""
Making a custom model viewset as to not repeat everytime I need a method
that will anyway be repeated in most cases.
"""
class CustomModelViewSet(ModelViewSet):
    
    # DRF comes equiped with base keywords for permissions and one can
    # arrange this simple method to setup permissions as they please
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    

    # PATCH is used by default for updating but in case i need it later, 
    # here is the default for PUT
    #def put(self, request, *args, **kwargs):
    #    return self.update(request, *args, **kwargs)