# Landing estatica simple, sin /docs/ gateado (a diferencia de
# Contalibra/Restolibra/Gestiolibra/MedLibra/VentaLibra, que ya tienen
# esa capa via la imagen compartida ghcr.io/marianocappucci/libra-nginx-web).
# LibraDesk todavia no tiene esa ronda -- ver README.md.
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY public/ /usr/share/nginx/html/
EXPOSE 80
