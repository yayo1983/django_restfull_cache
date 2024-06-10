from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Articulo
from .serializers import ArticuloSerializer

class ListaArticulos(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*2))  # Cachear la vista por 2 minutos
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
