from rest_framework import generics as g
from musica.models import Musica
from musica.api.serializers import MusicaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class MusicaListCreateAPIView(g.ListCreateAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'data']
    search_fields = ['nome', 'letra','banda__nome', 'participacoes__nome']
    ordering_fields = ['nome', 'banda__nome']
    ordering = ['nome']


class MusicaDetailAPIView(g.RetrieveUpdateDestroyAPIView):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'data']
    search_fields = ['nome', 'letra', 'banda__nome', 'participacoes__nome']
    ordering_fields = ['nome', 'banda__nome']
    ordering = ['nome']