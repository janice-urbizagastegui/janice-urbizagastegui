# Objetivo
Añadir tres micro‑interacciones sutiles para un look editorial premium sin comprometer performance: parallax suave en el Hero, zoom sutil al hover en la galería y fade‑up (opacidad + desplazamiento vertical) al entrar en viewport.

## Cambios CSS
- Fade‑up en items de galería:
  - Actualizar estado inicial a `opacity: 0; transform: translateY(20px);` y estado visible a `opacity: 1; transform: translateY(0);` (styles.css:45–46).
  - Ajustar `transition` a `opacity .5s ease-out, transform .5s ease-out` (styles.css:45).
- Zoom sutil en hover:
  - Añadir `transition: transform .8s ease; will-change: transform;` a `.gallery-img` (styles.css:47).
  - Añadir `transform: scale(1.02)` en hover: `.gallery-item:hover .gallery-img` y también cuando `.gallery-item.open` (para móvil)(nuevo bloque cerca de styles.css:50).
  - Asegurar que el recorte respete el borde redondeado: `overflow: hidden` en `.gallery-item` (styles.css:45).
- Hero CTA (ya mejorado) se mantiene; no se añaden animaciones extra para evitar ruido.
- Respetar accesibilidad: en `@media (prefers-reduced-motion: reduce)` desactivar transiciones y efectos (styles.css:61–65).

## Cambios JS
- Parallax en Hero:
  - Usar `requestAnimationFrame` con un listener `scroll` pasivo para calcular un offset suave (`offset = scrollY * 0.15`) y aplicarlo con `transform: translateY(offset * -1px)` sobre `.hero-image` (index.html:33; script.js nueva función `initParallaxHero`).
  - Clampear el valor para evitar desplazamientos excesivos en pantallas pequeñas.
  - Desactivar si `prefers-reduced-motion` es `reduce`.
- Fade‑up ya está soportado por IntersectionObserver; no se requiere JS adicional (script.js:75–85), solo el ajuste CSS.

## Performance y Accesibilidad
- `will-change: transform` en `.hero-image` y `.gallery-img` para optimización.
- Listener `scroll` pasivo + `requestAnimationFrame` para evitar jank.
- `prefers-reduced-motion` desactiva parallax y reduce transiciones.
- Sin cambios en carga (lazy/async) ni en SEO.

## Entregables
- Actualización de `styles.css` con zoom y fade‑up.
- Actualización de `script.js` con parallax suave.
- Verificación en `http://localhost:5500/` en mobile/desktop.

¿Autorizas aplicar estos cambios para elevar el impacto editorial manteniendo el rendimiento y la elegancia?