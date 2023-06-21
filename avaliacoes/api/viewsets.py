from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacoesSerializers

class AvaliacaoViewSet (ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializers
