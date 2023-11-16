from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Create your models here.

#class Company(models.Model):
    #name = models.CharField(max_length=50)
    #website = models.URLField(max_length=100)
    #foundation = models.PositiveIntegerField()

class UserManager(BaseUserManager):
    def create_user(self, correo, nombres, apellidos, dni, password=None):
        if not correo:
            raise ValueError('El campo correo es obligatorio')
        
        usuario= self.model(
            correo=self.normalize_email(correo),
            nombres=nombres,
            apellidos=apellidos,
            dni=dni,
            is_staff=True
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, correo, nombres, apellidos, dni, password, usuario_administrador=True):
        usuario= self.create_user(
            correo,
            nombres=nombres,
            apellidos=apellidos,
            dni=dni,
            is_staff=True,
            password=password
        )
        usuario.usuario_administrador = usuario_administrador
        usuario.save()
        return usuario
        
class Usuario(AbstractBaseUser):
    nombres = models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    dni=models.PositiveBigIntegerField()
    correo=models.EmailField(unique=True)
    is_staff=models.BooleanField(default=True)
    object = UserManager()
    
    USERNAME_FIELD= 'correo'
    REQUIRED_FIELDS = ['nombres','apellidos','dni']
    
class Policia(Usuario):
    rango=models.CharField(max_length=25)

    
class Ciudadano(Usuario):
    estado_civil=models.CharField(max_length=40)


class Vehiculo(models.Model):
    placa_vehicular=models.CharField(max_length=7)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=30)
    n_serie=models.CharField(max_length=18)
    n_motor=models.CharField(max_length=18)
    n_vin=models.CharField(max_length=18)
    color=models.CharField(max_length=30)
    placa_vigente=models.CharField(max_length=7)
    placa_anterior=models.CharField(max_length=7)
    estado=models.CharField(max_length=15)
    anotaciones=models.CharField(max_length=20)
    sede=models.CharField(max_length=20)
    propietarios=models.CharField(max_length=50)

class Reporte(models.Model):
    policia=models.ForeignKey(Policia, on_delete=models.CASCADE)
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora=models.DateTimeField(auto_now_add=True)
    descripcion=models.TextField()
    
class Denuncia(models.Model):
    ciudadano=models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora=models.DateTimeField(auto_now_add=True)
    descripcion=models.TextField()

class Registro_de_deteccion(models.Model):
    policia=models.ForeignKey(Policia, on_delete=models.CASCADE)
    ciudadano=models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora=models.DateTimeField(auto_now_add=True)
    ubicacion=models.CharField(max_length=30)
    placa_detectada=models.CharField(max_length=7)
    resultado_deteccion=models.TextField()
    confianza_deteccion=models.CharField(max_length=15)
    imagen_capturada=models.ImageField(upload_to='imagenes/registros/')
    