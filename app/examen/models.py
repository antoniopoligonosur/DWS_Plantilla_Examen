from django.db import models

# Create your models here.

#------------------------------- REFUGIO ------------------------------------------
class Refugio(models.Model):

    nombre= models.CharField(max_length=20)
    
#------------------------------- CENTRO ------------------------------------------ 
class Centro(models.Model):
    
    nombre= models.CharField(max_length=20)
    
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE, related_name='refugioCentro') 
    
#------------------------------- VACUNA ------------------------------------------ 
class Vacuna(models.Model):
    
    fabricante= models.CharField(max_length=20)
    nombre= models.CharField(max_length=20)
    
#------------------------------- ANIMAL ------------------------------------------ 
class Animal(models.Model):
    
    nombre= models.CharField(max_length=20)
    edad_estimada= models.PositiveIntegerField()
    
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE, related_name='centroAnimal')
    vacuna = models.ManyToManyField(Vacuna, blank=True, related_name='vacunasAnimal')

#------------------------------- REVISION_VETERINARIA ------------------------------------------ 
class Revision_veterinaria(models.Model):

    puntuacion_salud = models.PositiveIntegerField()
    fecha_revision = models.DateField(null=True, blank=True)
    veterinario = models.CharField(max_length=20)
    
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='animalRevisionVeterinaria')