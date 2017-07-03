from django.conf import settings
from .serializers import UserSerializer
from rest_framework import generics, status
from django.contrib.auth import authenticate
from uploader import key_config
from .models import AuthToken
from .serializers import UserLoginSerializer
from rest_framework.response import Response


class UserLogin(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kw):
        username = self.request.data.get(key_config.USERNAME_KEY)
        password = self.request.data.get(key_config.PASSWORD_KEY)

        user = authenticate(username=username, password=password)
        response = {}
        if user:
            auth_token = AuthToken.objects.create(user=user)
            if auth_token:
                response = UserLoginSerializer(auth_token).data
                return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(response, status=status.HTTP_200_OK)
