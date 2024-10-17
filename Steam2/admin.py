from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuario, Carrito, Biblioteca, Puntos, Distribuidora, Juego, Perfil, Tienda, Amigos, Coleccion

admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(Biblioteca)
admin.site.register(Puntos)
admin.site.register(Distribuidora)
admin.site.register(Juego)
admin.site.register(Perfil)
admin.site.register(Tienda)
admin.site.register(Amigos)
admin.site.register(Coleccion)
