FROM nginx:latest

COPY ./compose/nginx/production.conf /etc/nginx/conf.d/production.conf
COPY ./sdcurve/staticfiles /usr/share/nginx/html

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
