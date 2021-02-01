from rest_framework import serializers
from musica.models import Musica

class MusicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Musica
        fields = '__all__'


class MusicaResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musica
        fields = ['url', 'nome']