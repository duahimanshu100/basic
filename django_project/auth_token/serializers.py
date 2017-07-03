from rest_framework import serializers
from .models import AuthToken
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    '''
    Serializer for User.
    '''
    class Meta:
        '''
        Serializer customization
        '''
        model = User
        fields = ('id', 'username', 'email')
        # fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):

    '''
    Serializer for User.
    '''
    class Meta:
        '''
        Serializer customization
        '''
        model = AuthToken
        fields = ('token', 'user')

    def to_representation(self, data):
        data = super(UserLoginSerializer, self).to_representation(data)
        if data['user']:
            user = User.objects.filter(id=data['user']).first()
            if user:
                data['user'] = UserSerializer(user).data
        return data
