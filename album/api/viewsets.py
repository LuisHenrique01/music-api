from rest_framework import generics as g
from album.models import Album
from album.api.serializers import AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class AlbumListCreateAPIView(g.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends =  [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['data']
    search_fields = ['nome', 'banda__nome', 'musicas__nome']
    ordering_fields = ['data', 'banda__nome']
    ordering = ['data']
    

class AlbumRetrieveUpdateDestroyAPIView(g.RetrieveDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['data']
    search_fields = ['nome', 'banda__nome', 'musicas__nome']
    ordering_fields = ['data', 'banda__nome']
    ordering = ['data']
