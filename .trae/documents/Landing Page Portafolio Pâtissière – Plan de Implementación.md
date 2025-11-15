# Alcance de Implementación
Construir la estructura completa del sitio (HTML/CSS/JS) con contenido de placeholder: hero, galería asimétrica, sobre mí y contacto; listo para reemplazar imágenes y textos vía `images.json`.

## Decisiones Confirmadas
- Color de acento: `#B0A171`.
- Tipografías: Playfair Display (títulos) + Montserrat (texto).
- Placeholders: `via.placeholder.com` con proporciones mixtas (horizontal/vertical).

## Entregables
- `index.html` con secciones: Hero, Galería, Sobre Mí, Contacto.
- `styles.css` con variables de color/tipo, layout masonry responsive y micro-transiciones.
- `script.js` para: cargar `images.json`, renderizar galería, overlays (hover/tap), lazy/fade-in.
- `images/images.json` poblado con 12–15 items de ejemplo (lorem ipsum + URLs placeholder).

## Implementación Técnica
- Masonry por columnas (CSS `column-count` y `break-inside: avoid`) con 1→2→3 columnas por breakpoint.
- Overlay accesible: visible al hover (desktop) y tap (móvil), operable con teclado.
- Performance: `loading="lazy"`, `decoding="async"`, IntersectionObserver para fade-in, `defer` en JS, `preconnect` a Google Fonts.
- SEO/accesibilidad: semántica HTML5, `alt` descriptivos, OG/Twitter meta.

## Flujo de Actualización
- Para sustituir imágenes: colocar archivos en `/images/` y actualizar rutas en `images.json`.
- Para editar textos: modificar título/descripcion en `images.json`.

## Cronograma
- Día 1: scaffolding y hero.
- Día 2: galería y overlays.
- Día 3: optimización, accesibilidad y pulido.

¿Procedo a crear los archivos y dejar el sitio funcionando con placeholders?