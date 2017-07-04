from django.conf import settings
from .serializers import UserSerializer
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django_project import key_config
from .models import AuthToken
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class UserLogin(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kw):
        username = self.request.data.get(key_config.KEY_USERNAME)
        password = self.request.data.get(key_config.KEY_PASSWORD)

        user = authenticate(username=username, password=password)
        response = {}
        if user:
            auth_token = AuthToken.objects.create(user=user)
            if auth_token:
                response = UserLoginSerializer(auth_token).data
                return Response(response, status=status.HTTP_200_OK)
        else:
            response['error'] = ['Not Authorized']
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class UserSignUp(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kw):
        response = {}
        username = self.request.data.get(key_config.KEY_USERNAME)
        password = self.request.data.get(key_config.KEY_PASSWORD)
        first_name = self.request.data.get(key_config.KEY_FIRST_NAME)
        last_name = self.request.data.get(key_config.KEY_LAST_NAME)

        user = User.objects.filter(
            username__iexact=username)
        if user:
            response['error'] = ['User-name Already Exist']
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        else:
            now = timezone.now()
            extra_data = {'first_name': first_name, 'last_name': last_name}
            user = User(username=username, email=username,
                        is_staff=False, is_active=True,
                        is_superuser=False,
                        date_joined=now,
                        **extra_data)
            user.set_password(password)
            user.save()
            if user:
                auth_token = AuthToken.objects.create(user=user)
                if auth_token:
                    response = UserLoginSerializer(auth_token).data
                    return Response(response, status=status.HTTP_200_OK)

        response['error'] = ['Not Authorized']
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
