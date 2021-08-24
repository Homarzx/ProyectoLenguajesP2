from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
class Tienda(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    dueño=models.ForeignKey(Persona,on_delete=models.CASCADE)
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    stock=models.IntegerField()
    urlImagen=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)



    def __str__(self):
        return self.nombre

