from rest_framework.viewsets import ModelViewSet
from localizacoes.models import Localizacao
from localizacoes.api.serializers import LocalizacoesSerializers
class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacoesSerializers