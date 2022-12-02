from django.db import models

# Create your models here.

class Disco(models.Model):
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=20)
    tipo=models.CharField(max_length=20)
    precio=models.IntegerField()


class Impresora3D(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    tipo= models.CharField(max_length=20)
    precio=models.IntegerField()
        

class Compu(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    tipo= models.CharField(max_length=20)
    precio=models.IntegerField()





