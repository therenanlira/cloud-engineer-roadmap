# Solução do Desafio: Fundamentos (Módulo 1)

Este diretório contém a solução do primeiro desafio prático. O objetivo é unir **Linux, Redes, Automação em Python e Docker** para criar um monitor de conectividade de sites que entrega o relatório via contêiner Nginx.

## 🗂️ Arquivos do Projeto

- **`monitor.py`**: Script em Python que testa a conectividade dos sites e gera o arquivo `status.txt`.
- **`Dockerfile`**: Define a imagem Nginx, instala as dependências necessárias (Python/Pip) e gera o arquivo de status durante a construção da imagem.
- **`deploy.sh`**: Automatiza o build da imagem e o levantamento do contêiner.

## 🚀 Como executar esta solução

### 1. Dê permissão de execução ao script Bash

```bash
chmod +x deploy.sh
```

### 2. Execute o script de deploy

```bash
./deploy.sh
```

### 3. Valide o resultado

O script de deploy irá subir o servidor na porta 8080. Abra o seu navegador e acesse:

[http://localhost:8080/status.txt](http://localhost:8080/status.txt)

Você verá o relatório de "Online" ou "Offline" dos sites configurados no script.

## Limpando o ambiente

Para parar e remover o contêiner após os testes:

```bash
docker rm -f monitor-container
```

## Resumo do Aprendizado

Neste desafio, você praticou a base da engenharia de nuvem:

1. Python: Automação de tarefas e tratamento de erros de rede.
1. Docker: Criação de imagens, gestão de dependências (pip) e otimização de build.
1. Redes: Mapeamento de portas e comunicação HTTP.
1. Shell Script: Orquestração de todo o fluxo de trabalho.
