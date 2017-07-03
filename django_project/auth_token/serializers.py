from rest_framework import serializers
from .models import AuthToken
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):

    '''
    Serializer for User.
    '''
    class Meta:
        '''
        Serializer customization
        '''
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username', 'email')
        # fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):

    '''
    Serializer for User.
    '''
    users = UserSerializer(many=True)

    class Meta:
        '''
        Serializer customization
        '''
        model = AuthToken
        fields = ('user', 'token')
        depth = 1

    def to_representation(self, data):
        import pdb
        pdb.set_trace()
        super(UserLoginSerializer,self).to_representation(data)
