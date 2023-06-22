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
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank= True)

    @property
    def full_description_2 (self):
        return '%s ------------- %s' % (self.description, self.name)

    def __str__(self):
        return self.name