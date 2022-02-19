from django.db import models

# Create your models here.

class chela(models.Model):
    marca = models.CharField(max_length=50)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    minilitros = models.IntegerField()
    artesanal = models.BooleanField()
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    def nombre_chela(self):
        txt = "{0} de {1}"
        return txt.format(self.marca, self.nacionalidad)
    
    def __str__(self):
        return self.nombre_chela()
