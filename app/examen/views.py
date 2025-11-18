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

# URL 2 (DEVOLVER LISTA DE ANIMALES SEGUN FABRICANTE O NOMBRE DE VACUNA Y LA PUNTUACION DE SALUD DE REVISION VETERINARIA > 80)

def dame_animales_fabricante_vacuna(request, fabricanteVacuna, nombreVacuna):

    animales = (
        Animal.objects
        .select_related("centro__refugio")
        .prefetch_related("vacuna", "animalRevisionVeterinaria")
        .filter(Q(vacuna__fabricante = fabricanteVacuna)|Q(vacuna__nombre__icontains = nombreVacuna))
        .filter(animalRevisionVeterinaria__puntuacion_salud__gt=80)
        [:3].all()
    )

    return render(request, 'lista_animales.html',{'Animales_Mostrar':animales})

# URL 3 (DEVOLVER LISTA DE ANIMALES QUE NO TIENEN NINGUNA VACUNA ASIGNADA)

def dame_animales_animalVacuna_null(request):

    animales = (
        Animal.objects
        .select_related("centro__refugio")
        .prefetch_related("vacuna", "animalRevisionVeterinaria")  
        .filter(vacuna__id=None)
        .order_by('-edad_estimada')
        .all()
    )

    return render(request, 'lista_animales.html',{'Animales_Mostrar':animales})

# URL 4 (DEVOLVER LISTA DE REFUGIOS QUE TIENEN ANIMALES CON REVISION VETERINARIA EN UN AÑO DETERMINADO, ORDENADOS POR PUNTUACION DE SALUD DESCENDENTE)

def dame_refugios_anioRevision(request, anioRevision):

    refugios = (
        Refugio.objects
        .prefetch_related("refugioCentro__centroAnimal__animalRevisionVeterinaria")
        .filter(refugioCentro__centroAnimal__animalRevisionVeterinaria__fecha_revision__year=anioRevision)
        .order_by('-refugioCentro__centroAnimal__animalRevisionVeterinaria__puntuacion_salud')
        .all()
        .distinct()
    )

    return render(request, 'lista_refugios.html',{'Refugios_Mostrar':refugios})

# URL 5 (DEVOLVER LISTA DE ANIMALES DE UN CENTRO CONCRETO QUE TIENEN UNA MEDIA DE PUNTUACION DE SALUD MENOR QUE 50)

def dame_animales_centro_puntuacion(request, centroConcreto):

    animales = (
        Animal.objects
        .select_related("centro__refugio")
        .prefetch_related("vacuna", "animalRevisionVeterinaria")  
        .filter(centro__nombre=centroConcreto)
        .annotate(media = Avg("animalRevisionVeterinaria__puntuacion_salud"))
        .filter(media__lt=50)
        .all()
    )

    return render(request, 'lista_animales.html',{'Animales_Mostrar':animales})

# URL 6 (DEVOLVER LA ULTIMA REVISION VETERINARIA REALIZADA POR UN VETERINARIO CONCRETO A ANIMALES QUE HAN SIDO VACUNADOS CON UNA VACUNA DE UN FABRICANTE DETERMINADO Y QUE PERTENECEN A UN CENTRO DE UN REFUGIO CONCRETO)

def dame_animales_revision_veterinaria(request, veterinarioConcreto, fabricanteVacuna, centroRefugio):

    revisiones = (
        Revision_veterinaria.objects
        .select_related("animal__centro__refugio")
        .filter(veterinario = veterinarioConcreto)
        .filter(animal__vacuna__fabricante = fabricanteVacuna)
        .filter(animal__centro__nombre__icontains = centroRefugio)
        .order_by('-fecha_revision')[:1].get()
    )

    return render(request, 'revision_veterinaria.html',{'Revisiones_Mostrar':revisiones})

# Errores
def mi_error_404(request,exception=None):
    return render(request,'error/404.html',None,None,404)

def mi_error_403(request,exception=None):
    return render(request,'error/403.html',None,None,403)

def mi_error_400(request,exception=None):
    return render(request,'error/400.html',None,None,400)

def mi_error_500(request,exception=None):
    return render(request,'error/500.html',None,None,500)