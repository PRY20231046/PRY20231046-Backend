from django.contrib import admin
from django.urls import path
from .views import VehiculoView, DenunciaView

urlpatterns = [
    path('vehiculos/', VehiculoView.as_view(), name='vehiculos_list'),
    path('vehiculos/<int:id>', VehiculoView.as_view(), name='vehiculos_process'),
    path('denuncias/', DenunciaView.as_view(), name='vehiculos_process'),
    path('denuncias/<int:id>', DenunciaView.as_view(), name='vehiculos_process'),
    #path('placas/', ReconocimientoView.as_view(), name='placa_process'),
]