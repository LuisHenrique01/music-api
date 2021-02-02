from rest_framework import serializers
from album.models import Album
from musica.api.serializers import MusicaResumeSerializer

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Album
        fields = ['url', 'nome', 'banda', 'data', 'musicas']
