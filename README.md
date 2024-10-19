# Aplicacion Web Parte I Inicio y Modelos
Tarea de "Aplicación Web Parte 1 -Inicio y Modelos".

# Steam  2

-Mi página web estará basada en una plataforma de videojuegos en la nube, llamada Steam2.
Esta nueva versión de Steam permitirá a los usuarios acceder a sus juegos desde cualquier dispositivo con conexión a Internet, como ya hacen otros servicios de streaming como "Geforce now" sin necesidad de descargar ni instalar los juegos en sus equipos.Steam2 funcionará de manera similar a la plataforma original, pero con la ventaja de ofrecer streaming de videojuegos, lo que facilitará el acceso a los títulos en tiempo real, optimizando la experiencia de juego para aquellos con dispositivos de menor capacidad.La idea es que los usuarios puedan disfrutar de su biblioteca de juegos desde cualquier lugar y en cualquier momento, sin depender de hardware específico.

# Modelos de la Aplicación

### 1. Usuario
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre del usuario.
- **contraseña**: `CharField`, longitud máxima de 100 caracteres. Contraseña del usuario.
- **saldo**: `DecimalField`, máximo 10 dígitos y 2 decimales. Saldo disponible del usuario.
- **fecha_registro**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de registro del usuario.

**Relaciones**:
- Tiene un carrito (OneToOne con Carrito)
- Tiene una biblioteca (OneToOne con Biblioteca)
- Tiene puntos acumulados (OneToOne con Puntos)
- Puede tener múltiples perfiles (ManyToOne con Perfil)
- Puede tener múltiples amigos (ManyToMany con Amigos)
- Puede adquirir múltiples juegos (ManyToMany con Juego)

---

### 2. Carrito
- **usuario**: `OneToOneField`, referencia a Usuario. Usuario al que pertenece el carrito.
- **total_items**: `IntegerField`, por defecto 0. Total de juegos en el carrito.
- **total_precio**: `DecimalField`, máximo 10 dígitos y 2 decimales. Precio total de los juegos en el carrito.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación del carrito.

**Relaciones**:
- Pertenece a un usuario (OneToOne con Usuario)

---

### 3. Biblioteca
- **usuario**: `OneToOneField`, referencia a Usuario. Usuario al que pertenece la biblioteca.
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la biblioteca.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación de la biblioteca.
- **tamaño_total**: `IntegerField`, por defecto 0. Total de espacio disponible en la biblioteca.

**Relaciones**:
- Pertenece a un usuario (OneToOne con Usuario)

---

### 4. Puntos
- **usuario**: `OneToOneField`, referencia a Usuario. Usuario al que pertenecen los puntos.
- **puntos_acumulados**: `IntegerField`, por defecto 0. Total de puntos acumulados por el usuario.
- **fecha_expiracion**: `DateTimeField`. Fecha de expiración de los puntos acumulados.
- **nivel**: `IntegerField`, por defecto 0. Nivel del usuario basado en puntos acumulados.

**Relaciones**:
- Pertenece a un usuario (OneToOne con Usuario)

---

### 5. Distribuidora
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la distribuidora.
- **pais_origen**: `CharField`, longitud máxima de 100 caracteres, por defecto 'Desconocido'. País de origen de la distribuidora.
- **ingresos_anuales**: `DecimalField`, máximo 15 dígitos y 2 decimales. Ingresos anuales de la distribuidora.

**Relaciones**:
- Puede tener múltiples juegos (OneToMany con Juego)

---

### 6. Juego
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre del juego.
- **precio**: `DecimalField`, máximo 10 dígitos y 2 decimales. Precio del juego.
- **fecha_lanzamiento**: `DateTimeField`, puede ser nulo o estar en blanco. Fecha de lanzamiento del juego.
- **clasificacion_edad**: `IntegerField`, con opciones (0, 'Todos'), (12, '12+'), (16, '16+'), (18, '18+'). Clasificación por edad del juego.
- **distribuidora**: `ForeignKey`, referencia a Distribuidora. Distribuidora del juego.

**Relaciones**:
- Pertenece a una distribuidora (ManyToOne con Distribuidora)
- Puede estar en múltiples tiendas (ManyToMany con Tienda)

---

### 7. Perfil
- **usuario**: `ForeignKey`, referencia a Usuario. Usuario asociado al perfil.
- **alias**: `CharField`, longitud máxima de 100 caracteres. Alias del usuario en la plataforma.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación del perfil.
- **ultima_conexion**: `DateTimeField`, por defecto la fecha y hora actual. Última conexión del usuario.
- **visibilidad**: `BooleanField`, por defecto True. Visibilidad del perfil.

**Relaciones**:
- Pertenece a un usuario (ManyToOne con Usuario)

---

### 8. Tienda
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la tienda.
- **ofertas**: `TextField`, por defecto 'Sin ofertas'. Descripción de las ofertas en la tienda.
- **oferta_semanal**: `DateField`, por defecto 'Sin ofertas'. Fecha de la oferta semanal.
- **juegos**: `ManyToManyField`, referencia a Juego. Juegos disponibles en la tienda.

**Relaciones**:
- Puede tener múltiples juegos (ManyToMany con Juego)

---

### 9. Amigos
- **usuarios**: `ManyToManyField`, referencia a Usuario. Amigos de los usuarios.
- **nivel_amistad**: `IntegerField`. Nivel de amistad entre los usuarios.
- **interacciones_totales**: `IntegerField`. Total de interacciones entre los amigos.
- **mensaje_personalizado**: `CharField`, longitud máxima de 255 caracteres. Mensaje personalizado entre amigos.

**Relaciones**:
- Vínculo entre múltiples usuarios (ManyToMany con Usuario)

---

### 10. Colección
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la colección.
- **numero_juegos**: `IntegerField`, por defecto 0. Número total de juegos en la colección.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación de la colección.
- **bibliotecas**: `ManyToManyField`, referencia a Biblioteca a través de la tabla intermedia ColeccionBibliotecaJuego. Bibliotecas que contienen la colección.

**Relaciones**:
- Puede estar en múltiples bibliotecas (ManyToMany con Biblioteca a través de ColeccionBibliotecaJuego)

---

### 11. ColeccionBibliotecaJuego (Tabla intermedia)
- **coleccion**: `ForeignKey`, referencia a Coleccion. Colección a la que pertenece el juego.
- **biblioteca**: `ForeignKey`, referencia a Biblioteca. Biblioteca a la que pertenece el juego.
- **juego**: `ForeignKey`, referencia a Juego. Juego en la colección.
- **fecha_adicion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha en que el juego fue añadido a la colección.
- **comentario**: `TextField`, puede ser nulo o estar en blanco. Comentario adicional sobre el juego en la colección.

**Relaciones**:
- Vincula colecciones y bibliotecas con juegos (ManyToMany a través de la tabla intermedia)

  ---

## Modelo Entidad-Relación
(https://github.com/DavidRiosV/Aplicacion-Web-Parte-I-Inicio-y-Modelos/blob/main/EntidadRelacionSteam2.drawio.png)

  ---
  
## Explicación del Modelo ER

### 1. Relaciones (1,1)
- **Usuario - Carrito**: Un usuario tiene un carrito, y este carrito pertenece exclusivamente a ese usuario.
  - **Tipo de relación:** OneToOne.
  
- **Usuario - Biblioteca**: Un usuario tiene una biblioteca, y esa biblioteca es única y personal de cada usuario.
  - **Tipo de relación:** OneToOne.
  
- **Usuario - Puntos**: Los puntos acumulados por un usuario son exclusivos de ese usuario.
  - **Tipo de relación:** OneToOne.

---

### 2. Relaciones (1,M)
- **Juego - Distribuidora**: Cada juego pertenece a una única distribuidora, pero una distribuidora puede tener muchos juegos.
  - **Tipo de relación:** ManyToOne.

- **Perfil - Usuario**: Un perfil está asociado a un usuario, pero un usuario puede tener múltiples perfiles (por ejemplo, en diferentes juegos o grupos).
  - **Tipo de relación:** ManyToOne.

- **Juego - Tienda**: Los juegos pertenecen a una tienda, pero una tienda puede tener múltiples juegos a la venta.
  - **Tipo de relación:** ManyToOne.

---

### 3. Relaciones (M,M)
- **Usuario - Juegos**: Un usuario puede adquirir muchos juegos, y los juegos pueden ser adquiridos por muchos usuarios.
  - **Tipo de relación:** ManyToMany.

- **Usuario - Amigos**: Un usuario puede tener múltiples amigos, y cada amigo puede tener múltiples amigos en común con otros usuarios.
  - **Tipo de relación:** ManyToMany.

- **Colección - Biblioteca - Juegos**: Una biblioteca puede tener muchas colecciones, y una colección puede estar en muchas bibliotecas. Además, cada colección puede contener uno o más juegos.
  - **Tipo de relación:** ManyToMany (con tabla intermedia).

