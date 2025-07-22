# PATITAS.PET - Reto Final AWS

**Patitas.Pet** es una plataforma web diseñada para conectar a personas interesadas en adoptar animales con asociaciones de adopción. Este repositorio contiene los archivos principales del proyecto: HTML, CSS y JavaScript, que conforman la estructura, el diseño y la funcionalidad básica del sitio.

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

## Tecnologías Usadas  


| Tecnología           | Propósito                         |
|----------------------|-----------------------------------|
| Tailwind CSS         | Estilos rápidos y modernos        |
| GSAP + ScrollTrigger | Animaciones y transiciones        |
| Pinegrow Interactions| Configuración visual de efectos   |
| HTML5 / CSS3 / JS    | Estructura y funcionalidad base   |
