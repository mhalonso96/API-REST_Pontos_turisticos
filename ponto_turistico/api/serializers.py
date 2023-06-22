from rest_framework.serializers import ModelSerializer, SerializerMethodField
from ponto_turistico.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializers
from comentarios.api.serializers import ComentariosSerializers
from avaliacoes.api.serializers import AvaliacoesSerializers
from localizacoes.api.serializers import LocalizacoesSerializers
class PontoTuristicoSerializer(ModelSerializer):
    attraction = AtracoesSerializers(many= True)
    comment = ComentariosSerializers(many= True)
    review = AvaliacoesSerializers(many= True)
    placement = LocalizacoesSerializers()
    full_description = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ('id',
                  'name', 
                  'description', 
                  'approved', 
                  'photo',
                  'attraction',
                  'comment',
                  'review',
                  'placement',
                  'full_description',
                  'full_description_2',
                )
    def get_full_description(self, obj):
        return '%s - %s' % (obj.description, obj.name)
   