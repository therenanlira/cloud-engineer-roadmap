#!/bin/bash

# 1. Inicia o virtual env e instala a lib `requests`
# (Certifique-se de que o python3 está instalado no seu host)
python3 -m venv venv
source venv/bin/activate
python3 -m pip install requests 

# 2. Executa o script de monitoramento Python para gerar o arquivo status.txt
python3 monitor.py

# 3. Faz o build da imagem Docker
docker build -t monitor-site .

# 4. Para e remove container antigo, se existir
docker rm -f monitor-container 2>/dev/null

# 5. Sobe o novo container
docker run -d --name monitor-container -p 8080:80 monitor-site

echo "Deploy concluído! Acesse: http://localhost:8080/status.txt"
