from django.db import models

# Create your models here.

class Membro(models.Model):
    """Model definition for Membro."""

    nome = models.CharField('Nome', max_length=250)
    data_nascimento = models.DateField('Data Nascimento', null=True, blank=True)
    funcao = models.CharField('Função', max_length=250)

    class Meta:
        """Meta definition for Membro."""

        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        """Unicode representation of Membro."""
        return f'{self.nome}'
