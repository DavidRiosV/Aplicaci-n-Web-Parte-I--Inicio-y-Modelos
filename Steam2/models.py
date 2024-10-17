from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# Modelo Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    # Uso Decimal y no float ya que se supone que es exacto.
    # Con max_digits ajusto el valor maximo de digitos y con max_places ajusto el valor maximo de decimales
    fecha_registro = models.DateTimeField(default=timezone.now)

# Modelo Carrito
class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)
    total_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(default=timezone.now)

# Modelo Biblioteca
class Biblioteca(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    tamaño_total = models.IntegerField(default=0)

# Modelo Puntos
class Puntos(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    puntos_acumulados = models.IntegerField(default=0)
    fecha_expiracion = models.DateTimeField()
    nivel = models.IntegerField(default=0)

# Modelo Distribuidora
class Distribuidora(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100, default='Desconocido')
    ingresos_anuales = models.DecimalField(max_digits=15, decimal_places=2)

# Modelo Juego
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateTimeField(null=True, blank=True)
    clasificacion_edad = models.IntegerField(choices=[(0, 'Todos'), (12, '12+'), (16, '16+'), (18, '18+')])
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.CASCADE)

# Modelo Perfil
class Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    ultima_conexion = models.DateTimeField(default=timezone.now)
    visibilidad = models.BooleanField(default=True)

# Modelo Tienda
class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    ofertas = models.TextField(default='Sin ofertas')
    oferta_semanal = models.DateField(default='Sin ofertas')
    juegos = models.ManyToManyField(Juego)

# Modelo Amigos
class Amigos(models.Model):
    usuarios = models.ManyToManyField(Usuario)
    nivel_amistad = models.IntegerField()
    interacciones_totales = models.IntegerField()
    mensaje_personalizado = models.CharField(max_length=255)

# Modelo Coleccion
class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    numero_juegos = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    bibliotecas = models.ManyToManyField(Biblioteca, through='ColeccionBibliotecaJuego')

# Modelo intermedio ColeccionBibliotecaJuego
class ColeccionBibliotecaJuego(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    fecha_adicion = models.DateTimeField(default=timezone.now)  
    comentario = models.TextField(null=True, blank=True)



