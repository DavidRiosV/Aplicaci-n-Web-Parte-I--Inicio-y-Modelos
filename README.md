# Aplicacion Web Parte I Inicio y Modelos
Tarea de "Aplicación Web Parte 1 -Inicio y Modelos".

# Definir en qué consistirá mi página Web

##Steam  2
-Mi página web estará basada en una plataforma de videojuegos en la nube, llamada Steam2.
Esta nueva versión de Steam permitirá a los usuarios acceder a sus juegos desde cualquier dispositivo con conexión a Internet, como ya hacen otros servicios de streaming como "Geforce now" sin necesidad de descargar ni instalar los juegos en sus equipos.Steam2 funcionará de manera similar a la plataforma original, pero con la ventaja de ofrecer streaming de videojuegos, lo que facilitará el acceso a los títulos en tiempo real, optimizando la experiencia de juego para aquellos con dispositivos de menor capacidad.La idea es que los usuarios puedan disfrutar de su biblioteca de juegos desde cualquier lugar y en cualquier momento, sin depender de hardware específico.

## Modelos

### 1. Usuario
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre del usuario.
- **contraseña**: `CharField`, longitud máxima de 100 caracteres. Contraseña del usuario.
- **saldo**: `DecimalField`, máximo 10 dígitos y 2 decimales. Saldo disponible del usuario.
- **fecha_registro**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de registro del usuario.

**Relaciones**:
- Tiene un carrito (OneToOne con `Carrito`)
- Tiene una biblioteca (OneToOne con `Biblioteca`)
- Tiene puntos acumulados (OneToOne con `Puntos`)
- Puede tener múltiples perfiles (ManyToOne con `Perfil`)
- Puede tener múltiples amigos (ManyToMany con `Amigos`)
- Puede adquirir múltiples juegos (ManyToMany con `Juego` a través de la tabla intermedia)

### 2. Carrito
- **usuario**: `OneToOneField`, referencia a `Usuario`. Usuario al que pertenece el carrito.
- **total_items**: `IntegerField`. Total de juegos en el carrito.
- **total_precio**: `DecimalField`, máximo 10 dígitos y 2 decimales. Precio total de los juegos en el carrito.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación del carrito.

**Relaciones**:
- Pertenece a un usuario (OneToOne con `Usuario`)

### 3. Biblioteca
- **usuario**: `OneToOneField`, referencia a `Usuario`. Usuario al que pertenece la biblioteca.
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la biblioteca.
- **fecha_creacion**: `DateTimeField`, por defecto la fecha y hora actual. Fecha de creación de la biblioteca.
- **tamaño_total**: `IntegerField`. Total de espacio en la biblioteca.

**Relaciones**:
- Pertenece a un usuario (OneToOne con `Usuario`)

### 4. Puntos
- **usuario**: `OneToOneField`, referencia a `Usuario`. Usuario al que pertenecen los puntos.
- **puntos_acumulados**: `IntegerField`. Total de puntos acumulados por el usuario.
- **fecha_expiracion**: `DateTimeField`. Fecha de expiración de los puntos acumulados.
- **nivel**: `IntegerField`. Nivel del usuario basado en puntos acumulados.

**Relaciones**:
- Pertenece a un usuario (OneToOne con `Usuario`)

### 5. Distribuidora
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la distribuidora.
- **pais_origen**: `CharField`, longitud máxima de 100 caracteres. País de origen de la distribuidora.
- **ingresos_anuales**: `DecimalField`, máximo 15 dígitos y 2 decimales. Ingresos anuales de la distribuidora.

**Relaciones**:
- Puede tener múltiples juegos (OneToMany con `Juego`)

### 6. Juego
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre del juego.
- **precio**: `DecimalField`, máximo 10 dígitos y 2 decimales. Precio del juego.
- **fecha_lanzamiento**: `DateField`. Fecha de lanzamiento del juego.
- **clasificacion_edad**: `IntegerField`, con opciones definidas. Clasificación por edad del juego.
- **distribuidora**: `ForeignKey`, referencia a `Distribuidora`. Distribuidora del juego.

**Relaciones**:
- Pertenece a una distribuidora (ManyToOne con `Distribuidora`)
- Puede estar en múltiples tiendas (ManyToMany con `Tienda`)

### 7. Perfil
- **usuario**: `ForeignKey`, referencia a `Usuario`. Usuario asociado al perfil.
- **alias**: `CharField`, longitud máxima de 100 caracteres. Alias del usuario en la plataforma.
- **fecha_creacion**: `DateField`, por defecto la fecha actual. Fecha de creación del perfil.
- **ultima_conexion**: `TimeField`, por defecto la hora actual. Última hora de conexión del usuario.
- **visibilidad**: `BooleanField`, por defecto `True`. Visibilidad del perfil.

**Relaciones**:
- Pertenece a un usuario (ManyToOne con `Usuario`)

### 8. Tienda
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la tienda.
- **ofertas**: `TextField`. Descripción de las ofertas en la tienda.
- **oferta_semanal**: `DateField`. Fecha de la oferta semanal.
- **juegos**: `ManyToManyField`, referencia a `Juego`. Juegos disponibles en la tienda.

**Relaciones**:
- Puede tener múltiples juegos (ManyToMany con `Juego`)

### 9. Amigos
- **usuarios**: `ManyToManyField`, referencia a `Usuario`. Amigos de los usuarios.
- **nivel_amistad**: `IntegerField`. Nivel de amistad entre los usuarios.
- **interacciones_totales**: `IntegerField`. Total de interacciones entre los amigos.
- **mensaje_personalizado**: `CharField`, longitud máxima de 255 caracteres. Mensaje personalizado entre amigos.

**Relaciones**:
- Vínculo entre múltiples usuarios (ManyToMany con `Usuario`)

### 10. Colección
- **nombre**: `CharField`, longitud máxima de 100 caracteres. Nombre de la colección.
- **numero_juegos**: `IntegerField`. Número total de juegos en la colección.
- **fecha_creacion**: `DateField`, por defecto la fecha actual. Fecha de creación de la colección.
- **bibliotecas**: `ManyToManyField`, referencia a `Biblioteca`. Bibliotecas que contienen la colección.

**Relaciones**:
- Puede estar en múltiples bibliotecas (ManyToMany con `Biblioteca` a través de `ColeccionBibliotecaJuego`)

### 11. ColeccionBibliotecaJuego (Tabla intermedia)
- **coleccion**: `ForeignKey`, referencia a `Coleccion`. Colección a la que pertenece el juego.
- **biblioteca**: `ForeignKey`, referencia a `Biblioteca`. Biblioteca a la que pertenece el juego.
- **juego**: `ForeignKey`, referencia a `Juego`. Juego en la colección.

**Relaciones**:
- Vincula colecciones y bibliotecas con juegos (ManyToMany con tabla intermedia)
