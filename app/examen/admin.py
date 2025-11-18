from django.contrib import admin
from .models import Refugio, Centro, Vacuna, Animal, Revision_veterinaria 

# Register your models here.

admin.site.register(Refugio)
admin.site.register(Centro) 
admin.site.register(Vacuna) 
admin.site.register(Animal) 
admin.site.register(Revision_veterinaria)