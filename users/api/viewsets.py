from rest_framework import generics as g
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer, AdminUserSerializer
from users.api.permissions import UsuarioPermission


class UserCreateAPIView(g.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    
class UserRetrieveUpdateDestroyAPIView(g.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UsuarioPermission]
    
    
class AdminUserCreateAPIView(g.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]