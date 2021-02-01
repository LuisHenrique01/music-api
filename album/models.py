from django.db import models
from banda.models import Banda
from membro.models import Membro
from musica.models import Musica
# Create your models here.

class Album(models.Model):
    """Model definition for Album."""

    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=250)
    data = models.DateField('Data')
    musicas = models.ManyToManyField(Musica, related_name='musicas')
    
    class Meta:
        """Meta definition for Album."""

        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

    def __str__(self):
        """Unicode representation of Album."""
        return f'{self.nome}' # TODO
