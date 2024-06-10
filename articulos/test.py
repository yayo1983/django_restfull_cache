from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Articulo

class ArticuloAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.articulo_url = reverse('lista_articulos')

    def test_create_articulo(self):
        data = {'titulo': 'Nuevo Artículo', 'descripcion': 'Nueva Descripción'}
        response = self.client.post(self.articulo_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_articulos(self):
        Articulo.objects.create(titulo="Artículo 1", descripcion="Descripción 1")
        response = self.client.get(self.articulo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
