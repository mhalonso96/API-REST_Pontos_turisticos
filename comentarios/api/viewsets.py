from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from comentarios.api.serializers import ComentariosSerializers

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializers