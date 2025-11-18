from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('lista/animales/<str:nombreAnimal>/<str:nombreRefugio>',views.dame_animales_nombre_refugio, name='dame_animales_nombre_refugio'),
    path('lista/animales/<str:fabricanteVacuna>/<str:nombreVacuna>',views.dame_animales_fabricante_vacuna, name='dame_animales_fabricante_vacuna'),
    path('lista/animales-con-AnimalVacuna-None/',views.dame_animales_animalVacuna_null, name='dame_animales_animalVacuna_null'),
    path('lista/refugios/<int:anioRevision>',views.dame_refugios_anioRevision, name='dame_refugios_anioRevision'),
    path('lista/animales/<str:centroConcreto>',views.dame_animales_centro_puntuacion, name='dame_animales_centro_puntuacion'),
    path('revision_veterinaria/<str:veterinarioConcreto>/<str:fabricanteVacuna>/<str:centroRefugio>',views.dame_animales_revision_veterinaria, name='dame_animales_revision_veterinaria'),
]