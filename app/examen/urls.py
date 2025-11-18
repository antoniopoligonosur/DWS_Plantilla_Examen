from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('lista/animales/<str:nombreAnimal>/<str:nombreRefugio>',views.dame_animales_nombre_refugio, name='dame_animales_nombre_refugio'),
]