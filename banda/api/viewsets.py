from rest_framework import generics as g
from banda.api.serializers import BandaSerializer
from banda.models import Banda
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BandaListCreateAPIView(g.ListCreateAPIView):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['membros__nome', 'nome']
    ordering_fields = ['data', 'nome']
    ordering = ['nome']
    

class BandaRetrieveUpdateDestroyAPIView(g.RetrieveUpdateDestroyAPIView):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['membros__nome', 'nome']
    ordering_fields = ['data', 'nome']
    ordering = ['nome']