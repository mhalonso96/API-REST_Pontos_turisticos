from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracoesSerializers(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'name', 'description', 'opening_hours', 'minimum_age', 'photo', )