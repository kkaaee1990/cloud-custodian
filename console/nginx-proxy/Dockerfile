FROM nginx:alpine

RUN apk add apache2-utils

COPY htpasswd /etc/nginx/
COPY nginx.conf /etc/nginx/
COPY index.html /usr/share/nginx/html