#!/bin/bash

# 1. Faz o build da imagem Docker
docker build -t monitor-site .

# 2. Para e remove container antigo, se existir
docker rm -f monitor-container 2>/dev/null

# 3. Sobe o novo container
docker run -d --name monitor-container -p 8080:80 monitor-site

echo "Deploy concluído! Acesse: http://localhost:8080/status.txt"
