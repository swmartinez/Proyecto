from django.db import models


class Curso(models.Model): #La clase Curso hereda todas las propiedasdes de models.Model

    nombre = models.CharField(max_length=40) #Hay que indicar que tipo de dato van a tener las variables en la base de datos
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
