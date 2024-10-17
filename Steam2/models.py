from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(default=timezone.now)

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)
    total_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(default=timezone.now)

class Biblioteca(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    tamaño_total = models.IntegerField(default=0)

class Puntos(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    puntos_acumulados = models.IntegerField(default=0)
    fecha_expiracion = models.DateTimeField()
    nivel = models.IntegerField(default=0)

class Distribuidora(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100, default='Desconocido')
    ingresos_anuales = models.DecimalField(max_digits=15, decimal_places=2)

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateTimeField(null=True, blank=True)
    clasificacion_edad = models.IntegerField(choices=[(0, 'Todos'), (12, '12+'), (16, '16+'), (18, '18+')])
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.CASCADE)

class Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    ultima_conexion = models.DateTimeField(default=timezone.now)
    visibilidad = models.BooleanField(default=True)

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    ofertas = models.TextField()
    oferta_semanal = models.DateField()
    juegos = models.ManyToManyField(Juego)

class Amigos(models.Model):
    usuarios = models.ManyToManyField(Usuario)
    nivel_amistad = models.IntegerField()
    interacciones_totales = models.IntegerField()
    mensaje_personalizado = models.CharField(max_length=255)

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    numero_juegos = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    bibliotecas = models.ManyToManyField(Biblioteca, through='ColeccionBibliotecaJuego')

class ColeccionBibliotecaJuego(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)

