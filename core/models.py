from django.db import models


class Filmes(models.Model):
    nome = models.CharField(max_length=40)
    mes = models.CharField(max_length=10)
    ano = models.IntegerField(default=0)
    genero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    receita = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.nome
