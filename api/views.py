from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Vehiculo
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