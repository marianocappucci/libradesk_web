# LibraDesk — Sitio Web / Landing

Landing page de marketing para [LibraDesk](https://libradesk.com.ar), soporte
técnico e incidencias IT (clientes, equipos, incidencias). Mismo patrón que
`contalibra_web`/`restolibra_web`/`gestiolibra_web`/`medlibra_web`/
`ventalibra_web`: HTML estático servido por nginx en un contenedor Docker.

## Estado actual

- Landing completa: hero, módulos con badges por plan, para quién, cómo
  funciona, planes y precios, CTA de contacto y footer con el resto de la
  familia Libra.
- **CI/CD** (`.github/workflows/deploy.yml`): push a `main` dispara rsync al
  VPS + rebuild de Docker (reusa `libra-web-kit/.github/workflows/deploy-vps.yml`,
  el mismo reusable workflow que los otros 5 sitios). Requiere el secret
  `VPS_DEPLOY_KEY` cargado en el repo.
- **Deploy real al VPS + proxy NPM/SSL para el apex** `libradesk.com.ar`.

## Diferencia deliberada con el resto de la familia

Los otros 5 sitios tienen `/docs/` gateado por login (imagen compartida
`ghcr.io/marianocappucci/libra-nginx-web` + servicio `auth` de
`libra-web-kit`). **Esta ronda de LibraDesk no incluye esa capa** — alcance
explícito, decidido con el usuario: solo landing + CI/CD + deploy real.
`Dockerfile` usa `nginx:1.27-alpine` liso con un `nginx.conf` propio (sin
`auth_request`, sin servicio `auth`), para no depender de un endpoint
`/auth/verify` que la app LibraDesk todavía no tiene. Agregar `/docs/`
gateado queda pendiente para una ronda futura, siguiendo el mismo patrón que
el resto de la familia (ver `wiki/entities/libradesk.md`, sección
"Problemas conocidos / pendientes").

## Desarrollo local

Sin Docker disponible en WSL local — verificar con:

```bash
cd public && python3 -m http.server 8088
```

En el VPS, `docker compose build && docker compose up -d` (puerto host
`8088`, requiere la red externa `stack_stack-net`).

## Estructura

```
public/
  index.html          — Landing completa
  css/style.css        — Generado por libra-web-kit/scripts/generate_css.py, NO EDITAR A MANO
  img/                  — (vacío por ahora, sin foto de hero propia)
Dockerfile              — FROM nginx:1.27-alpine
nginx.conf              — gzip, try_files, headers de seguridad (sin auth_request)
docker-compose.yml      — servicio web (8088:80), red stack_stack-net
.github/workflows/
  deploy.yml            — CI/CD rsync al VPS + docker compose rebuild
```

## CSS compartido

`public/css/style.css` se genera desde `libra-web-kit` (mismo mecanismo que
Contalibra/Restolibra/Gestiolibra/MedLibra/VentaLibra):

```bash
cd ~/proyectos/libra-web-kit
.venv/bin/python scripts/generate_css.py
```

Paleta propia: índigo (`--brand: #4f46e5`), token `libradesk` en
`libra_web_kit/site_css_tokens.py`.

## Relacionado

- Producto documentado: [LibraDesk](https://github.com/marianocappucci/libradesk)
- Mismo patrón: `contalibra_web`, `restolibra_web`, `gestiolibra_web`,
  `medlibra_web`, `ventalibra_web`
