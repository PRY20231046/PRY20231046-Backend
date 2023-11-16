from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Reporte, Vehiculo, Denuncia, Ciudadano
import json
import base64
import io
from PIL import Image
import numpy as np
import cv2
import imutils
import easyocr
# Create your views here.
def decodificar_imagen_base64(imagen_base64):
        
        try:
            # Decodifica la cadena base64 en una representación binaria de la imagen
            imagen_binaria = base64.b64decode(imagen_base64)
        
            # Crea un objeto de imagen utilizando la biblioteca Pillow (PIL)
            imagen = Image.open(io.BytesIO(imagen_binaria))
        
            # Convierte la imagen en un arreglo numpy (si es necesario)
            imagen_numpy = np.array(imagen)

            return imagen_numpy
        
        except Exception as e:
            # Maneja cualquier excepción que pueda ocurrir al decodificar la imagen
            print(f"Error al decodificar la imagen base64: {str(e)}")
            return None
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

class ReconocimientoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request):
        jd = json.loads(request.body)
        imagen_codificada = jd['imagen_base64']
        imagen = decodificar_imagen_base64(imagen_codificada)
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(bfilter, 30, 200)
        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break
        print(location)
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(imagen, imagen, mask=mask)
        
        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+1, y1:y2+1]
        reader = easyocr.Reader(['es'])
        result = reader.readtext(cropped_image)
        print(result)
        placa = result[1][-2]
        
        if placa:
            print(placa)
            datos= {'Placa': placa}
        else:
            datos = {'message': "No se encontro codigo de placa"}
             
        return JsonResponse(datos)