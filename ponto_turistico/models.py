from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacoes.models import Localizacao

class PontoTuristico(models.Model):
    name = models.CharField(max_length= 255)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Atracao)
    comment = models.ManyToManyField(Comentario)
    review = models.ManyToManyField(Avaliacao)
    placement = models.ForeignKey(Localizacao, on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
        return self.name