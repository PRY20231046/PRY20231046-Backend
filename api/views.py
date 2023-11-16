from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Reporte, Vehiculo, Denuncia, Ciudadano
import json
# Create your views here.

class VehiculoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            vehiculos = list(Vehiculo.objects.filter(id=id).values())
            if len(vehiculos)>0:
                vehiculo = vehiculos[0]
                datos = {'message': "Success", 'vehiculo': vehiculo}
            else:
                datos = {'message': "No se encontro vehiculo registrado ..."}
            return JsonResponse(datos)
        else:
            vehiculos = list(Vehiculo.objects.values())
            if len(vehiculos)>0:
                datos = {'message': "Success", 'vehiculos': vehiculos}
            else:
                datos = {'message': "No se encontraron vehiculos registrados ..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Vehiculo.objects.create(placa_vehicular=jd['placa_vehicular'], marca= jd['marca'], modelo=jd['modelo'], n_serie=jd['n_serie'], n_motor=jd['n_motor'], n_vin=jd['n_vin'], color=jd['color'], placa_vigente=jd['placa_vigente'], placa_anterior=jd['placa_anterior'], estado=jd['estado'], anotaciones=jd['anotaciones'], sede=jd['sede'], propietarios=jd['propietarios'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        vehiculos = list(Vehiculo.objects.filter(id=id).values())
        if len(vehiculos)>0:
            vehiculo = Vehiculo.objects.get(id=id)
            vehiculo.placa_vehicular=jd['placa_vehicular']
            vehiculo.marca= jd['marca'] 
            vehiculo.modelo=jd['modelo'] 
            vehiculo.n_serie=jd['n_serie']
            vehiculo.n_motor=jd['n_motor']
            vehiculo.n_vin=jd['n_vin']
            vehiculo.color=jd['color']
            vehiculo.placa_vigente=jd['placa_vigente']
            vehiculo.placa_anterior=jd['placa_anterior']
            vehiculo.estado=jd['estado']
            vehiculo.anotaciones=jd['anotaciones']
            vehiculo.sede=jd['sede']
            vehiculo.propietarios=jd['propietarios']
            vehiculo.save()
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro vehiculo registrado ..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        vehiculos = list(Vehiculo.objects.filter(id=id).values())
        if len(vehiculos)>0:
            Vehiculo.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro vehiculo registrado ..."}
        return JsonResponse(datos)

class DenunciaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            denuncias = list(Denuncia.objects.filter(id=id).values())
            if len(denuncias)>0:
                denuncia = denuncias[0]
                datos = {'message': "Success", 'denuncia': denuncia}
            else:
                datos = {'message': "No se encontro denuncia registrado ..."}
            return JsonResponse(datos)
        else:
            denuncias = list(Denuncia.objects.values())
            if len(denuncias)>0:
                datos = {'message': "Success", 'denuncias': denuncias}
            else:
                datos = {'message': "No se encontraron denuncias registrados ..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Denuncia.objects.create(ciudadano=jd['ciudadano'], vehiculo= jd['vehiculo'], fecha_hora=jd['fecha_hora'], descripcion=jd['descripcion'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        denuncias = list(Denuncia.objects.filter(id=id).values())
        if len(denuncias)>0:
            denuncia = Denuncia.objects.get(id=id)
            denuncia.ciudadano=jd['ciudadano']
            denuncia.vehiculo= jd['vehiculo'] 
            denuncia.fecha_hora=jd['fecha_hora'] 
            denuncia.descripcion=jd['descripcion']
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro denuncia registrado ..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        denuncias = list(Denuncia.objects.filter(id=id).values())
        if len(denuncias)>0:
            Vehiculo.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro denuncia registrado ..."}
        return JsonResponse(datos)

class ReporteView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            reportes = list(Reporte.objects.filter(id=id).values())
            if len(reportes)>0:
                reporte = reportes[0]
                datos = {'message': "Success", 'reporte': reporte}
            else:
                datos = {'message': "No se encontro reporte registrado ..."}
            return JsonResponse(datos)
        else:
            reportes = list(Reporte.objects.values())
            if len(reportes)>0:
                datos = {'message': "Success", 'reportes': reportes}
            else:
                datos = {'message': "No se encontraron reporte registrados ..."}
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Reporte.objects.create(policia=jd['policia'], vehiculo= jd['vehiculo'], fecha_hora=jd['fecha_hora'], descripcion=jd['descripcion'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        reportes = list(Reporte.objects.filter(id=id).values())
        if len(reportes)>0:
            reporte = Reporte.objects.get(id=id)
            reporte.policia=jd['policia']
            reporte.vehiculo= jd['vehiculo'] 
            reporte.fecha_hora=jd['fecha_hora'] 
            reporte.descripcion=jd['descripcion']
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro reporte registrado ..."}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        reportes = list(Reporte.objects.filter(id=id).values())
        if len(reportes)>0:
            Vehiculo.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message': "No se encontro reporte registrado ..."}
        return JsonResponse(datos)