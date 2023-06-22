from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from atracoes.api.serializers import AtracoesSerializers
from atracoes.models import Atracao

class AtracaoViewSet (ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializers
    filter_fields = ('name', 'description')
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )