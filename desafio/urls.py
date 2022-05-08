from django.urls import path
from .views import *
urlpatterns = [
    path('/', familiarestemp),
    path('/agregar', agregar, name= 'agregar'),
    path('/borrar/<id>', borrar, name= 'borrar')
]