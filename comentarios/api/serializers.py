from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
class ComentariosSerializers (ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'user', 'comment', 'date', 'approved')