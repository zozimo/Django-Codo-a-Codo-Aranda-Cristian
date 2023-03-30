from django.db import models

# Create your models here.
# Se crea una clase por cada tabla que necesitamos en la base de datos.
# Esto es útil porque posteriormente se ejecutara el codigo necesario
# para el motor de la base de datos que elijamos, por lo tanto nos abstrae
# de la sintaxis especifica de cada motor
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    def __str__(self) -> str:
        return f'El nombre es {self.nombre}, la seccion  {self.seccion} y el precio es{self.precio}'
    # def __str__(self):
    #     return 'El nombre es %s, la sección %s y el precio %s'%(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
