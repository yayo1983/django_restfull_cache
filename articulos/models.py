from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
