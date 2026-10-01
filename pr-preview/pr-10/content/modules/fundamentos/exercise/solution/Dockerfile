FROM nginx:alpine

# Instala python e gerenciador de pacotes
RUN apk add --no-cache python3 py3-pip

# Instala a biblioteca requests
RUN pip3 install requests --break-system-packages

# Copia o script Python e roda para gerar o status.txt
COPY monitor.py .
RUN python3 monitor.py && mv status.txt /usr/share/nginx/html/status.txt

EXPOSE 80
