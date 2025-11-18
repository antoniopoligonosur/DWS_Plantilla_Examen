from django.shortcuts import render
from django.views.defaults import page_not_found
from .models import Refugio, Centro, Animal, Vacuna, Revision_veterinaria
from django.db.models import Q , Prefetch, Avg, Max, Min

# Create your views here.

def index(request):
    return render(request, 'index.html')

# URL 1 (DEVOLVER LISTA DE ANIMALES SEGUN NOMBRE Y REFUGIO)

def dame_animales_nombre_refugio(request, nombreAnimal, nombreRefugio):

    animales = (
        Animal.objects
        .select_related("centro__refugio")
        .prefetch_related("vacuna")
        .filter(nombre__icontains = nombreAnimal, centro__refugio__nombre = nombreRefugio)
        .all()
    )

    return render(request, 'lista_animales.html',{'Animales_Mostrar':animales})

# Errores
def mi_error_404(request,exception=None):
    return render(request,'error/404.html',None,None,404)

def mi_error_403(request,exception=None):
    return render(request,'error/403.html',None,None,403)

def mi_error_400(request,exception=None):
    return render(request,'error/400.html',None,None,400)

def mi_error_500(request,exception=None):
    return render(request,'error/500.html',None,None,500)