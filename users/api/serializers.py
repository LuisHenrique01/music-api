from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        return User(**validated_data)
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        return instance
        
        
class AdminUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser']
        
    def create(self, validated_data):
        user = User(username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.is_superuser = True
        user.save()
        return User(**validated_data)
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        return instance