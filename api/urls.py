from django.contrib import admin
from django.urls import path
from .views import VehiculoView

urlpatterns = [
    path('vehiculos/', VehiculoView.as_view(), name='vehiculos_list'),
    path('vehiculos/<int:id>', VehiculoView.as_view(), name='vehiculos_process'),
]