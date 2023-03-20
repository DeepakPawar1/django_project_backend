from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.user.serializers import UserSerializer
from core.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch','get')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        print("in get querysetrr")
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    def get_object(self):
        print("in get object")
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        print(obj,";;;;")
        self.check_object_permissions(self.request,obj)
        return obj


