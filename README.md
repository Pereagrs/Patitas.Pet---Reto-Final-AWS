# PATITAS.PET - Reto Final AWS

**Patitas.Pet** es una plantilla moderna y responsiva desarrollada para organizaciones sin fines de lucro que promueven la adopción de mascotas. Está construida sobre tecnologías potentes como **Tailwind CSS**, **GSAP** y **Pinegrow Interactions**, permitiendo un diseño atractivo y animaciones fluidas, con estilos personalizados que hacen que cada componente luzca profesional y amigable.

# WEB
## HTML (`index.html`)
Página web principal del proyecto con varios animales disponibles.
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
Hoja de estilos de la página web principal del proyecto.
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
Archivo JS de la página principal del proyecto.
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

## Perfil Animal en adopción (`Adoptme.html`)
Sitio web estático desarrollado en HTML, CSS y JavaScript. Su estructura incluye un header con navegación, una galería de imágenes responsiva, una sección de perfil con información detallada de los perros y un formulario de adopción funcional. El diseño visual está implementado con CSS puro, utilizando tipografía de Google Fonts, layout basado en grid y flexbox, colores coherentes y efectos de sombreado para un aspecto limpio y moderno.

El formulario de adopción captura datos del usuario (nombre, teléfono, email y mensaje) y los envía mediante fetch a una API REST externa en formato JSON, mostrando mensajes de confirmación o error según la respuesta. Además, la página es completamente adaptable a dispositivos móviles gracias a media queries.

## Página de registro de animales (`AñadirAnimal.html`)
Web estática desarrollada con HTML, CSS y JavaScript, orientada al registro de nuevos animales para adopción. Incluye una barra de navegación con enlaces principales, un formulario organizado en tarjetas para ingresar datos del animal (nombre, edad, tamaño, descripción e imagen) y un botón de guardado.

El diseño está implementado con CSS puro, utilizando tipografía de Google Fonts, layout basado en grid y componentes visuales con bordes redondeados, sombras y colores consistentes, asegurando una experiencia clara y atractiva.

En el apartado funcional, la imagen del animal se carga a un bucket S3 mediante una URL prefirmada obtenida desde una API externa. Los datos del formulario se validan en el cliente antes de enviarlos, y pueden integrarse posteriormente con una base de datos como DynamoDB para su almacenamiento. La estructura es completamente adaptable a dispositivos móviles gracias al uso de estilos flexibles.

## Perfil de protectora con integración en Cognito (`PerfilProtectoras.html`)

Interfaz web estática construida con HTML, CSS y JavaScript que muestra el perfil de una protectora de animales. Incluye una barra de navegación, un avatar central, y una tarjeta de perfil con campos editables como correo electrónico, teléfonos, ubicaciones y descripción de la organización.

El diseño está implementado con CSS puro, utilizando tipografía de Google Fonts, un layout basado en grid para organizar los datos, y estilos visuales modernos con bordes redondeados y sombras para mejorar la experiencia del usuario.

La funcionalidad de edición de perfil está integrada con Amazon Cognito. Al pulsar "Editar perfil", el sistema obtiene la sesión activa del usuario y actualiza los atributos en el User Pool de Cognito mediante el SDK amazon-cognito-identity-js. De esta forma, los datos quedan vinculados directamente al usuario autenticado.

## Panel de gestión de animales para protectoras (`Protectoras.html`)
Web estática creada con HTML, Tailwind CSS y JavaScript. Presenta un dashboard de bienvenida con navegación superior, un grid dinámico de tarjetas para mostrar animales gestionados por una protectora, y un modal para editar la información de cada animal.

La maquetación utiliza clases utilitarias de Tailwind para estilos responsivos, tipografía clara y componentes modernos con sombras, bordes redondeados y notificaciones (como el contador de mensajes). Las tarjetas de animales se generan dinámicamente desde un array en JavaScript, mostrando imagen, nombre y descripción.

Además, incluye un modal para la edición de datos de animales que se activa al hacer clic en el botón de edición de cada tarjeta. La estructura está preparada para integrarse con una API de backend que permita guardar los cambios en una base de datos.

## Pantalla de inicio de sesión de Patitas.Pet (`login.html`)
La página es una interfaz de inicio de sesión estática desarrollada en HTML y CSS con soporte parcial de Tailwind para tipografía y espaciados. Su diseño aplica un fondo de imagen a pantalla completa y una tarjeta central con estilo _glassmorphism_ (fondo semitransparente con difuminado), generando un efecto moderno y limpio.

El formulario de autenticación incluye campos para correo electrónico y contraseña, un botón de inicio de sesión estilizado y un enlace de registro. La estructura es sencilla, fácilmente integrable con servicios de autenticación externos como AWS Cognito o Firebase.
## Pantalla de registro de usuarios de Patitas.Pet (`registro.html`)
La página es un formulario de registro desarrollado en HTML y Tailwind CSS con un diseño _glassmorphism_ centrado en pantalla. Incluye campos para nombre, correo electrónico y contraseña, todos con validación requerida.

Integra la librería **Amazon Cognito Identity JS**, lo que permite conectar el formulario con AWS Cognito para gestionar el alta de usuarios. El diseño es completamente responsivo, con animación de entrada suave y estilos optimizados para una experiencia moderna y clara.
## Registro de usuarios con AWS Cognito (`registro.js`)
Este fragmento de JavaScript implementa la lógica de registro de usuarios para tu formulario de **registro de Patitas.Pet** con **AWS Cognito**. Explicación breve y clara:

### **Cómo funciona**
1.  **Intercepción del formulario:**

    -   Se escucha el evento `submit` del formulario `#registro-form` y se evita el envío por defecto (`e.preventDefault()`).
        
2.  **Obtención de datos:**
    
    -   Se capturan los valores de **nombre**, **correo electrónico** y **contraseña** desde los inputs correspondientes.
        
3.  **Configuración de AWS Cognito:**
    
    -   Se define el `UserPoolId` y `ClientId` del **User Pool** de Cognito.
        
4.  **Definición de atributos de usuario:**
    
    -   Se crea una lista de atributos:
        
        -   `email` (estándar de Cognito).
            
        -   `custom:nombre` (atributo personalizado en Cognito).
            
5.  **Registro en Cognito:**
    
    -   Se llama a `userPool.signUp()` con los datos del usuario.
        
    -   Si hay error, se muestra un `alert` con el mensaje.
        
    -   Si es exitoso, se notifica al usuario y se redirige a la pantalla de login.

El usuario se registra en tu **User Pool de Cognito** con los atributos configurados y debe confirmar su cuenta desde el email recibido.

# FUNCIONES

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
## Función Lambda: Enviar correos con Amazon SES (`Funcion Enviar Correo.py`)
Este código implementa una función AWS Lambda que recibe datos desde un evento HTTP (API Gateway) y envía un correo electrónico utilizando Amazon Simple Email Service (SES). Funcionalidad:

-Procesa una petición HTTP con un body en formato JSON que contiene:
	
 - nombre: nombre del remitente.
 - email: correo del remitente.
 - mensaje: texto del mensaje.
 - animal: nombre del animal sobre el que se consulta.

-Envía un correo electrónico a una dirección predefinida usando SES.
-Devuelve una respuesta JSON indicando si el envío fue exitoso o si ocurrió un error.

## Función Lambda: Enviar solicitudes de adopción por email usando Cognito y SES (`EnviarSolicitudAdopcion.py`)
Esta función Lambda en AWS recibe los datos de una solicitud de adopción enviados desde la web, incluyendo nombre, teléfono, email, mensaje y el ID de la protectora.
Primero consulta el User Pool de Cognito para obtener el correo electrónico asociado a esa protectora usando su ID.
Luego, utiliza Amazon SES para enviar un email a la protectora con la información de la solicitud, incluyendo los datos del interesado y su mensaje.
Finalmente, responde con un mensaje de éxito si el correo se envía correctamente, o un error si ocurre algún problema durante el proceso.
## Función Lambda: Exportación automatizada de tabla DynamoDB a S3 (`Funcion ExportTableToPointInTime.py`)
Esta función Lambda exporta una tabla DynamoDB a un bucket de S3 configurado vía variables de entorno.  
Usa la API `export_table_to_point_in_time` para crear una exportación en formato JSON de DynamoDB, con un prefijo que incluye la fecha y hora actual para identificar la exportación.  
El ARN de la tabla se construye dinámicamente usando la región y el ID de cuenta extraídos del contexto de ejecución.  
Devuelve un mensaje de éxito con el ARN de la exportación iniciada o un error si la operación falla.
## Función Lambda: Asignación automática de grupo a usuario tras confirmación en Cognito (`Funcion PostConfirmation.py`)
Este código es una función Lambda que se activa después de que un usuario confirma su registro en un User Pool de AWS Cognito (evento PostConfirmation_ConfirmSignUp). Su función es añadir automáticamente al usuario confirmado al grupo "PatitasPetUsers" dentro del User Pool especificado. Esto permite gestionar fácilmente permisos y roles para los usuarios recién registrados, asegurando que tengan los accesos adecuados desde el primer momento.
## Función Lambda: Flujo completo de envío y registro de solicitudes de adopción (`Función envío y registro de solicitudes de adopción.json`)
Esta función gestiona el proceso integral de envío de solicitudes de adopción, registrando los datos del solicitante en una base de datos DynamoDB y notificando automáticamente a la protectora correspondiente mediante un correo electrónico enviado con AWS SES. Así se garantiza tanto el almacenamiento seguro de la información como la comunicación inmediata para agilizar el proceso de adopción.
## Función Lambda: Asignación automática de grupo a usuario tras confirmación en Cognito (`PostConfirmationUpdate.py`)
El primer código "PostConfirmation" es una función que, tras confirmar el registro de un usuario en Cognito, lo añade a un grupo y además guarda sus datos (incluyendo atributos personalizados) en una tabla DynamoDB, con manejo de errores. Este segundo código, unido al anterior, añade el asignar al usuario al grupo en Cognito y no registra datos adicionales ni gestiona errores. 
# POLÍTICAS

## Política de configuración de acceso S3 (`Politica json solo lectura.json`)
Este archivo contiene una política de control de acceso para habilitar la lectura pública de los archivos estáticos del proyecto alojados en **Amazon S3**. Descripción general:
-Permitir que cualquier usuario (Principal: `"*"`) pueda acceder a los objetos almacenados en el bucket S3 `patitas-pet-frontend`.
-Acción permitida: `s3:GetObject` — habilita exclusivamente la lectura de archivos, sin autorización para escritura o eliminación.
-Recurso afectado: Todos los archivos dentro del bucket `patitas-pet-frontend`.
## Política de subida de imágenes a S3 desde Lambda (`Política de bucket s3PutObject.py`)
Este archivo JSON define una política de permisos que permite a una función Lambda asumir el rol LabRole y subir archivos al bucket S3 patitas-imagenes.

Esta política debe aplicarse a la configuración de políticas del bucket S3 `patitas-imagenes`, permitiendo así que funciones Lambda asociadas al rol `LabRole` puedan subir imágenes, por ejemplo, como parte de un flujo de carga de imágenes en una aplicación como **Patitas.Pet**.

## Política de confianza para un rol de AWS IAM (`Política de confianza Rol IAM.json`)
Define una política de confianza para un rol de AWS IAM, permitiendo que usuarios autenticados de un Identity Pool de Amazon Cognito asuman el rol mediante STS (Security Token Service). Esta política garantiza que únicamente los usuarios autenticados a través de Cognito puedan obtener credenciales temporales de IAM para acceder a los recursos definidos por el rol.
## Política IAM: Acceso a S3 (`Politica acceso al bucket S3 rol IAM.json`)
Esta política concede a un usuario, rol o servicio permisos específicos sobre el bucket `patitas-imagenes`. Se asigna esta política a roles de Lambda u otros servicios que necesiten leer, listar y escribir imágenes en el bucket de S3.
## Política IAM: Permiso para enviar correos con Amazon SES (`Politica permisos SES a la Lambda.json`)
Esta política otorga a la entidad (usuario, grupo o rol) el permiso para enviar correos electrónicos utilizando **Amazon Simple Email Service (SES)**. Se asigna esta política a un rol o usuario que necesite enviar correos electrónicos mediante Amazon SES.
## Política de permisos S3 para exportación de DynamoDB (`Politica PatitasDynamoDBBackupAccess.json`)
Esta política de bucket de Amazon S3 permite que el rol DynamoDBExportRole tenga acceso al bucket patitas-backups-dynamo para exportar datos de DynamoDB. 
Permisos otorgados:

 - s3:PutObject → Subir objetos al bucket.
 - s3:GetObject → Leer objetos del bucket.
 - s3:ListBucket → Listar el contenido del bucket

Recursos:

 - Bucket: arn:aws:s3:::patitas-backups-dynamo
 - Objetos del bucket: arn:aws:s3:::patitas-backups-dynamo/*

Con esta configuración, el rol autorizado puede realizar exportaciones de tablas DynamoDB directamente al bucket especificado.

## Política IAM para Permitir la Adición de Usuarios a Grupos en Cognito (`Permiso Lambda a Cognito.json`)
Esta política concede permiso para ejecutar la acción AdminAddUserToGroup en un User Pool específico de AWS Cognito. Permite que un rol o usuario IAM administre la asignación de usuarios a grupos dentro del User Pool identificado por su ARN, facilitando así la gestión de grupos y roles en la autenticación de usuarios.
## Política IAM para Permitir Escritura en la Tabla DynamoDB "Protectoras" (`PermisoPut_Protectoras.json`)
Esta política permite la acción `PutItem` sobre la tabla DynamoDB llamada "Protectoras" en la región us-east-1. Autoriza a un rol o usuario IAM a insertar o actualizar elementos en dicha tabla, facilitando la gestión y almacenamiento de datos relacionados con protectoras dentro de la base de datos.
# SCRIPTS
## Script para creación de alarmas en AWS CloudWatch para funciones Lambda (`Script creación alarmas AWS CloudWatch para funciones Lambda.ps1`)
Este script de PowerShell crea alarmas de CloudWatch para funciones AWS Lambda y configura un tema de SNS para recibir notificaciones por correo electrónico cuando se detecten errores.

Funcionalidades
-Crea automáticamente un tema SNS si no existe.
-Suscribe un correo electrónico al tema SNS para recibir alertas.
-Configura alarmas de CloudWatch para múltiples funciones Lambda.
-Cada alarma se activa si se detecta al menos 1 error en el periodo configurado.

Es necesario confirmar la suscripción por email para comenzar a recibir alertas.
Requiere AWS Tools for PowerShell v4 o superior.