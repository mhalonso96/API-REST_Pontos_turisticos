from rest_framework.serializers import ModelSerializer
from localizacoes.models import Localizacao

class LocalizacoesSerializers(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('id', 'line1', 'line2', 'city', 'state', 'country')

    