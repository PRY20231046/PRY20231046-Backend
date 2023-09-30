from django.contrib import admin
from .models import Policia,Ciudadano,Vehiculo,Registro_de_deteccion,Reporte,Denuncia

# Register your models here.

#admin.site.register(Company)
admin.site.register(Policia)
admin.site.register(Ciudadano)
admin.site.register(Vehiculo)
admin.site.register(Registro_de_deteccion)
admin.site.register(Reporte)
admin.site.register(Denuncia)