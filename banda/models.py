from django.db import models
from membro.models import Membro

class Banda(models.Model):
    """Model definition for Banda."""

    membros = models.ManyToManyField(Membro, related_name='bandas')
    nome = models.CharField('Nome', max_length=250)
    data = models.DateField('Data fundação', null=True, blank=True)

    class Meta:
        """Meta definition for Banda."""

        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'

    def __str__(self):
        """Unicode representation of Banda."""
        return f'{self.nome}'


# Create your models here.
