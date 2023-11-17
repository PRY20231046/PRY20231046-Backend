from django.contrib import admin
from django.urls import path
from .views import VehiculoView, DenunciaView, ReporteView

urlpatterns = [
    path('vehiculos/', VehiculoView.as_view(), name='vehiculos_list'),
    path('vehiculos/<int:id>', VehiculoView.as_view(), name='vehiculos_process'),
    path('denuncias/', DenunciaView.as_view(), name='denuncias_process'),
    path('denuncias/<int:id>', DenunciaView.as_view(), name='denuncias_process'),
    path('reportes/', ReporteView.as_view(), name='reportes_process'),
    path('reportes/<int:id>', ReporteView.as_view(), name='reportes')
    #path('placas/', ReconocimientoView.as_view(), name='placa_process'),
]