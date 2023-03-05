from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
#from django.contrib.auth.models import User
from users.models import iLKMSUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = iLKMSUser
        fields = ('id','full_name' ,'email','phone_number', 'password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = iLKMSUser.objects.create_user(full_name = validated_data['full_name'], password = validated_data['password']  ,email=validated_data['email'],  phone_number=validated_data['phone_number'], date_of_birth = None, national_id = None, address = None)
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = iLKMSUser
        fields = '__all__'