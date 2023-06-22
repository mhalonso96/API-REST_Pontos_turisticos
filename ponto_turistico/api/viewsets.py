from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PontoTuristicoViewSet (ModelViewSet):
    
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name','placement__line1')
    #lookup_field = 'name' altera de id para nome
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset= queryset.filter(pk=id)
        if name:
            queryset= queryset.filter(name__iexact=name)
        if description:
            queryset= queryset.filter(description__iexact=description)
        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    