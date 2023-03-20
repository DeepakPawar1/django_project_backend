
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer
from django.db import transaction
import json
class RegisterViewSet(ViewSet):
   serializer_class = RegisterSerializer
   permission_classes = (AllowAny,)
   http_method_names = ['post']
   def create(self, request, *args, **kwargs):
       serializer =self.serializer_class(data=request.data)
       serializer.is_valid(raise_exception=True)
       try:
         with transaction.atomic():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            }
            response_dict = dict()
            response_dict['user'] = serializer.data
            response_dict['refresh'] = res['refresh']
            response_dict['access'] = res['access']
            return Response(response_dict, status=201)
       except Exception as e:
            print("in exception for error",e)
            return Response({"Error has ocures"},status = 500)
       