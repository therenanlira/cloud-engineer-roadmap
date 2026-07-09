---
layout: default
title: Fundamentos (Desafio - Solução)
---

# Cloud Engineer Roadmap (DevOps/SRE/Platform)

Um guia de estudos para iniciantes de Cloud Engineer (DevOps/SRE/Platform) **gratuitos** e em **português**, com **laboratórios** e **desafios** para você evoluir a cada etapa.

---

## 1. Fundamentos

A base técnica indispensável: sistemas operacionais, redes, automação e contêineres.

## Solução para o desafio prático (Fundamentos)

O objetivo deste desafio é unir **Linux, Redes, Automação em Python e Docker** para criar um monitor de conectividade de sites que entrega o relatório via contêiner Nginx.

### 1. Script Python

Crie o script `monitor.py`. Ele testa a conectividade de uma lista de sites usando a biblioteca `requests` e salva o resultado formatado no arquivo `status.txt`.

```python
{% include_relative monitor.py %}
```

### 2. Dockerfile

Crie o arquivo `Dockerfile`. Ele parte da imagem oficial do `nginx`, instala o Python e a biblioteca `requests`, copia o script para dentro da imagem e o executa durante o build, deixando o `status.txt` já pronto na pasta que o Nginx serve.

```Dockerfile
{% include_relative Dockerfile %}
```

### 3. Script de deploy

Crie o script `deploy.sh`. Ele é o "maestro" que automatiza toda a sequência: prepara o ambiente Python, gera o `status.txt`, faz o build da imagem e sobe o contêiner.

```bash
{% include_relative deploy.sh %}
```

Dê permissão de execução e rode o script:

```bash
chmod +x deploy.sh
./deploy.sh
```

### 4. Valide o resultado

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

{% include next-steps.html
   prev_url="/content/modules/fundamentos/lab/"
   prev_title="Desafio (Fundamentos)"
   next_url="/content/modules/cloud/"
   next_title="Cloud"
%}
