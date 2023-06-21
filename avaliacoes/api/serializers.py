from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao
class AvaliacoesSerializers (ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comment', 'note', 'date')
