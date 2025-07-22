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
## CSS (`style.txt`)
- Incluye `tailwind.css` con extensiones personalizadas.
- Tipografía: **Space Grotesk** vía Google Fonts.
- Modificadores de Tailwind extendidos, con clases personalizadas como:
  - `bg-primary-500`, `text-secondary-500`, `hover:text-primary-600`, entre otros.
- Animaciones responsivas y clases adaptadas para diferentes resoluciones (`md:`, `lg:`, `xl:`).
- Fondo interactivo con imágenes desde Unsplash aplicadas a la clase `.poster:before`.
- Compatibilidad con elementos interactivos (`hover`, `focus`, `disabled`, etc.)
- Clases definidas para:
  - Espaciado, tamaño, color, borde, display, tipografía, efectos responsivos y opacidad.
## JavaScript (`script.txt`)
- Carga el **Pinegrow Interactions Runtime 2.14**.
- Integra animaciones con la librería **GSAP**.
- Control de eventos:
  - `pgObserver`: gestos, desplazamiento, clics.
  - `pgScrollTrigger`: activa animaciones según el scroll.
  - `pgClass`, `pgDom`, `pgCall`: gestión del DOM y clases CSS.
- Aplicación de presets de animaciones como `fadeInUp`, `bounce`, `zoomIn`, etc.
- Adaptación automática para elementos con `data-pg-ia`.
## Configuración de acceso S3 (`Politica json solo lectura.json`)
Este archivo contiene una política de control de acceso para habilitar la lectura pública de los archivos estáticos del proyecto alojados en **Amazon S3**. Descripción general:
-Permitir que cualquier usuario (Principal: `"*"`) pueda acceder a los objetos almacenados en el bucket S3 `patitas-pet-frontend`.
-Acción permitida: `s3:GetObject` — habilita exclusivamente la lectura de archivos, sin autorización para escritura o eliminación.
-Recurso afectado: Todos los archivos dentro del bucket `patitas-pet-frontend`.
## Función Lambda: Crear Animal (`Funcio crear animal.py`)
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
## Configuración PWA (`PWA Enlaza archivos en el index.html`)

Este fragmento HTML activa las funcionalidades de **Progressive Web App (PWA)** en el sitio web, permitiendo una experiencia más cercana a una app móvil, incluso sin conexión.

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

## Tecnologías Usadas  


| Tecnología           | Propósito                         |
|----------------------|-----------------------------------|
| Tailwind CSS         | Estilos rápidos y modernos        |
| GSAP + ScrollTrigger | Animaciones y transiciones        |
| Pinegrow Interactions| Configuración visual de efectos   |
| HTML5 / CSS3 / JS    | Estructura y funcionalidad base   |
