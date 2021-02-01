from rest_framework import serializers
from banda.models import Banda
from membro.api.serializers import MembroSerializer

class BandaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Banda
        fields = ['nome', 'data', 'membros']