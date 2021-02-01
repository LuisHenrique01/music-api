from django.db import models
from banda.models import Banda
from membro.models import Membro

# Create your models here.
class Musica(models.Model):
    """Model definition for Musica."""

    nome = models.CharField('Nome', max_length=250)
    letra = models.TextField(blank=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    participacoes = models.ManyToManyField(Membro, related_name='participacoes', blank=True)
    data = models.DateField('Data', auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        """Meta definition for Musica."""

        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'

    def __str__(self):
        """Unicode representation of Musica."""
        return f'{self.nome}' # TODO
