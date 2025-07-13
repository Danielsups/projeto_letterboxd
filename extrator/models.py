from django.db import models

class Filme(models.Model):
    # O campo 'id' é criado automaticamente pelo Django como AutoField e chave primária.
    nomeFilme = models.CharField(max_length=255)
    anoFilme = models.IntegerField(null=True, blank=True)
    sinopseFilme = models.TextField(blank=True)
    duracaoFilme = models.IntegerField(null=True, blank=True) # Duração em minutos
    diretorFilme = models.CharField(max_length=255, blank=True)
    notaFilme = models.FloatField(null=True, blank=True)
    avaliacoesFilme = models.IntegerField(null=True, blank=True)
    urlFilme = models.URLField(max_length=500)

    def __str__(self):
        return self.nomeFilme