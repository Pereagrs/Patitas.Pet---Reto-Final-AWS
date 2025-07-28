# PATITAS.PET - Reto Final AWS

**Patitas.Pet** es una plantilla moderna y responsiva desarrollada para organizaciones sin fines de lucro que promueven la adopción de mascotas. Está construida sobre tecnologías potentes como **Tailwind CSS**, **GSAP** y **Pinegrow Interactions**, permitiendo un diseño atractivo y animaciones fluidas, con estilos personalizados que hacen que cada componente luzca profesional y amigable.

# Archivos
## HTML (`index.html`)
- Estructura semántica y responsiva con Tailwind.
- Secciones destacadas:
  - **Header**: enlaces de navegación y redes sociales.
  - **Hero**: mensaje principal y botón de adopción.
  - **Galería**: tarjetas de mascotas con nombres, descripciones y botones.
  - **Estadísticas**: número de animales adoptados, voluntarios, etc.
  - **Footer**: enlaces útiles y una galería secundaria.
## HTML de Error 404 personalizada (`404.html`)
Este archivo HTML muestra una página de error **404 - Página no encontrada**, diseñada para mejorar la experiencia del usuario cuando intenta acceder a una URL inexistente en la aplicación.
-   **Diseño responsive** y minimalista. 
-   **Estilo CSS embebido** para facilitar su uso sin archivos externos.
-   **Compatible** con la mayoría de navegadores modernos.
## CSS (`style.css`)
- Incluye `tailwind.css` con extensiones personalizadas.
- Tipografía: **Space Grotesk** vía Google Fonts.
- Modificadores de Tailwind extendidos, con clases personalizadas como:
  - `bg-primary-500`, `text-secondary-500`, `hover:text-primary-600`, entre otros.
- Animaciones responsivas y clases adaptadas para diferentes resoluciones (`md:`, `lg:`, `xl:`).
- Fondo interactivo con imágenes desde Unsplash aplicadas a la clase `.poster:before`.
- Compatibilidad con elementos interactivos (`hover`, `focus`, `disabled`, etc.)
- Clases definidas para:
  - Espaciado, tamaño, color, borde, display, tipografía, efectos responsivos y opacidad.
## JavaScript (`script.js`)
- Carga el **Pinegrow Interactions Runtime 2.14**.
- Integra animaciones con la librería **GSAP**.
- Control de eventos:
  - `pgObserver`: gestos, desplazamiento, clics.
  - `pgScrollTrigger`: activa animaciones según el scroll.
  - `pgClass`, `pgDom`, `pgCall`: gestión del DOM y clases CSS.
- Aplicación de presets de animaciones como `fadeInUp`, `bounce`, `zoomIn`, etc.
- Adaptación automática para elementos con `data-pg-ia`.
## Configuración PWA (`PWA Enlaza archivos en el index.html`)

Este fragmento HTML activa las funcionalidades de **Progressive Web App (PWA)** en el sitio web, permitiendo una experiencia más cercana a una app móvil, incluso sin conexión. La eliminación se realiza solo si el `animal_id` existe en el registro mediante la expresión condicional `attribute_exists(animal_id)`. El flujo de la función es el siguiente:

### Archivos involucrados

- `manifest.json`: Define los metadatos de la PWA.
  - Nombre de la aplicación.
  - Iconos para diferentes resoluciones.
  - Color de fondo y tema.
  - Pantalla inicial y comportamiento al abrirse.
- `service-worker.js`: Script que gestiona el caché de los recursos y habilita la funcionalidad offline.
  - Precarga archivos HTML, CSS, JS y medios.
  - Actualiza dinámicamente los recursos del sitio.
  - Maneja eventos como instalación y activación.

## Función Lambda: Crear Animal (`Funcion crear animal.py`)
Esta función Lambda escrita en **Python** permite registrar nuevos animales en la base de datos de **Amazon DynamoDB**, vinculándolos a una protectora específica. Realiza lo siguiente:

- **Recibe** datos JSON desde una petición HTTP (API Gateway).
- **Valida** los campos requeridos: `protectora_id`, `nombre`, y `especie`.
- **Genera** un identificador único para el animal si no se proporciona.
- **Crea** un objeto con todos los atributos del animal.
- **Guarda** el registro en la tabla `Animales` de DynamoDB.
- **Devuelve** una respuesta con estado HTTP y el `animal_id` generado.

### Campos utilizados

El animal que se inserta en la base de datos incluye:

| Campo          | Descripción                             |
|----------------|-----------------------------------------|
| `protectora_id`| ID de la protectora asociada            |
| `animal_id`    | Identificador único del animal          |
| `nombre`       | Nombre del animal                       |
| `especie`      | Especie (perro, gato, etc.)             |
| `edad`         | Edad (opcional)                         |
| `tamaño`       | Tamaño (opcional)                       |
| `estado`       | Estado del animal (por defecto: disponible) |
| `foto_url`     | Enlace a imagen representativa (opcional) |
| `descripcion`  | Texto descriptivo breve (opcional)      |
| `creado_en`    | Fecha de creación (ISO UTC)             |

### Validaciones y errores
- Si faltan datos obligatorios, se devuelve un error 400 con mensaje detallado.
- Si ocurre algún fallo interno, se responde con estado 500 y mensaje genérico.
## Función Lambda: Eliminar Animal (`Funcion Borrar animal.py`)
La función procesa una solicitud HTTP (evento API Gateway) con un cuerpo JSON que contiene dos campos obligatorios: `protectora_id` y `animal_id`. Si ambos están presentes, se intenta eliminar el ítem correspondiente en la tabla `Animales`.

- **Parseo del cuerpo** recibido en formato JSON.
-    **Validación** de campos obligatorios (`protectora_id`, `animal_id`).
-    **Eliminación del ítem** en la tabla DynamoDB si existe.
-   **Respuesta JSON** con código 200 si se elimina correctamente.
-    **Manejo de errores** con código 400 (faltan campos) o 500 (error interno).
## Función Lambda: Editar Animal (`Funcion Editar animal.py`)
Este script en Python implementa una función AWS Lambda para actualizar los detalles de un animal registrado en una tabla DynamoDB, ideal para sistemas de gestión de protectoras de animales. El flujo de trabajo es el siguiente:
- **Recepción del evento** La función recibe un evento HTTP (normalmente vía API Gateway) con un cuerpo JSON que contiene el `protectora_id`, `animal_id` y los campos a actualizar.
- **Parseo del cuerpo JSON** El contenido del `event['body']` se transforma en un diccionario de Python usando `json.loads()`.
- **Validación de campos obligatorios** Se verifica que existan `protectora_id` y `animal_id`.
    
    -   Si alguno falta ➝ se retorna `400 Bad Request` con un mensaje de error.
        
- **Preparación de expresión de actualización**: Se inicia con la actualización del campo `actualizado_en` con la hora actual en formato ISO. Se recorren los campos potencialmente actualizables (`nombre`, `especie`, `edad`, `tamaño`, `estado`, `foto_url`, `descripcion`) y se añaden dinámicamente si están presentes en el cuerpo.
        
- **Validación de campos a actualizar**: Si **ninguno** de los campos actualizables fue proporcionado ➝ se retorna `400 Bad Request`.
- **Actualización del ítem en DynamoDB**: Se ejecuta el método `update_item()`.
                
	-	**Respuesta exitosa**: Si todo va bien, retorna `200 OK` con el mensaje: `"Animal actualizado correctamente."`
        
	- **Manejo de errores** : Si ocurre una excepción durante el proceso ➝ se captura y se responde con `500 Internal Server Error`.
 
## Función Lambda: UploadURL (`Funcion generarUploadURL.py`)
La función  recibe un JSON vía API Gateway que incluye el tipo de contenido (ej. `image/jpeg`) y devuelve:

-   Una **URL prefirmada** para subir la imagen.
-   Una **URL pública** donde estará accesible la imagen una vez subida.

Flujo de trabajo:
- **Parseo del cuerpo JSON**: Se obtiene el tipo de contenido (content_type) y se valida que sea una imagen (image/*).

- **Validación del tipo de archivo**: Si no es imagen ➝ responde 400 Bad Request.

- **Generación de nombre único de archivo**: Se crea un nombre con UUID y extensión correspondiente, en la carpeta animales/.

- **Generación de URL prefirmada**: Se usa generate_presigned_url con validez de 1 hora (ExpiresIn: 3600).

- **Respuesta con URLs**:

	- **upload_url**: para subir la imagen.

	- **file_url**: la URL pública donde estará la imagen.

- **Manejo de errores**: Si ocurre algún problema, responde con 500 Internal Server Error.

## Política de configuración de acceso S3 (`Politica json solo lectura.json`)
Este archivo contiene una política de control de acceso para habilitar la lectura pública de los archivos estáticos del proyecto alojados en **Amazon S3**. Descripción general:
-Permitir que cualquier usuario (Principal: `"*"`) pueda acceder a los objetos almacenados en el bucket S3 `patitas-pet-frontend`.
-Acción permitida: `s3:GetObject` — habilita exclusivamente la lectura de archivos, sin autorización para escritura o eliminación.
-Recurso afectado: Todos los archivos dentro del bucket `patitas-pet-frontend`.
## Política de subida de imágenes a S3 desde Lambda (`Política de bucket s3PutObject.py`)
Este archivo JSON define una política de permisos que permite a una función Lambda asumir el rol LabRole y subir archivos al bucket S3 patitas-imagenes.

Esta política debe aplicarse a la configuración de políticas del bucket S3 `patitas-imagenes`, permitiendo así que funciones Lambda asociadas al rol `LabRole` puedan subir imágenes, por ejemplo, como parte de un flujo de carga de imágenes en una aplicación como **Patitas.Pet**.


## Tecnologías Usadas  


| Tecnología           | Propósito                         |
|----------------------|-----------------------------------|
| Tailwind CSS         | Estilos rápidos y modernos        |
| GSAP + ScrollTrigger | Animaciones y transiciones        |
| Pinegrow Interactions| Configuración visual de efectos   |
| HTML5 / CSS3 / JS    | Estructura y funcionalidad base   |