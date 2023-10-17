from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.text import slugify

class Sector(models.Model):
    idSector = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class MiUsuarioManager(BaseUserManager):
    def normalize_dpi(self, dpi):
        return slugify(dpi)  
    def create_user(self, dpi, password=None, **extra_fields):
        if not dpi:
            raise ValueError('El campo DPI debe ser establecido')
    
        dpi = self.normalize_dpi(dpi)
        user = self.model(dpi=dpi, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, dpi, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(dpi, password, **extra_fields)




class MiUsuario(AbstractBaseUser):
    email = models.CharField(max_length=255)
    nombres_apellidos = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    sector_ubicacion = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    titular = models.CharField(max_length=255)
    dpi = models.CharField(max_length=20, unique=True)  # Cambia el campo email a dpi
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MiUsuarioManager()

    USERNAME_FIELD = 'dpi'

class Anuncio(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Fontanero(models.Model):
    idfontanero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    dpi = models.CharField(max_length=20, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')
    
    TIPO_PAGO_CHOICES = [
        ('Semanal', 'Semanal'),
        ('Mensual', 'Mensual'),
        ('Quincenal', 'Quincenal'),
    ]
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO_CHOICES, default='Semanal')

    def __str__(self):
        return self.nombre




class Predio(models.Model):
    idpredio = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=255)
    
    ESTADO_CHOICES = [
        ('Vendido', 'Vendido'),
        ('Disponible', 'Disponible'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Disponible')
    
    dueño = models.ForeignKey(MiUsuario(), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Predio ID: {self.idpredio}, Ubicación: {self.ubicacion}"
    

class Jornales(models.Model):
    idJornal = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Multas(models.Model):
    idmultas = models.AutoField(primary_key=True)  
    descripcion = models.TextField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    pago_realizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Multas ID: {self.idmultas}, Saldo: {self.saldo}"


class PagoAgua(models.Model):
    idpagoagua = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(MiUsuario, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pago_realizado = models.BooleanField(default=False)
    mes = models.CharField(max_length=255)  

    def __str__(self):
        return f"Usuario: {self.usuario.nombres_apellidos}, Saldo: {self.saldo}, Mes: {self.mes}"
    
    

 







    


