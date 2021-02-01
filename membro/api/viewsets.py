from rest_framework import generics as g
from membro.api.serializers import MembroSerializer
from membro.models import Membro
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class MembroListCreateAPIView(g.ListCreateAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'data_nascimento']
    search_fields = ['nome']
    ordering_fields = ['nome', 'data_nascimento']
    ordering = ['nome']


class MembroRetrieveUpdateDestroyAPIView(g.RetrieveUpdateDestroyAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer
    permission_classes = [IsAdminUser,]
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'data_nascimento']
    search_fields = ['nome']
    ordering_fields = [ 'nome', 'data_nascimento']
    ordering = ['nome']