from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Supermercado(models.Model):
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField() 
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='productos/')
    origen = models.URLField()  
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre 
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=300)
    calificacion = models.IntegerField() 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'producto') 



