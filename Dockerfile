# Imagen base compartida con Contalibra/Restolibra/Gestiolibra/MedLibra/
# VentaLibra: trae el gateo de /docs/ (login, auth_request y rate limit) y el
# nginx.conf comun -- ver wiki/entities/libra-web-kit.md.
#
# 🔴 Hasta el 2026-08-06 esta landing NO usaba esta base y no tenia /docs/:
# figuraba en el wiki como "diferencia deliberada". El humano pidio que la
# tenga, asi que se alinea con las otras cinco en vez de duplicar el gateo.
# AUTH_UPSTREAM se setea via docker-compose.yml.
FROM ghcr.io/marianocappucci/libra-nginx-web:v0.2.0
COPY public/ /usr/share/nginx/html/
EXPOSE 80
