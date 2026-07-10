---
layout: default
title: Fundamentos (Desafio)
---

# 1. Fundamentos

A base técnica indispensável: sistemas operacionais, redes, automação e contêineres.

## Desafio Prático (Fundamentos)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para o reforçar o conhecimento.

**Objetivo**: Juntar os seus conhecimentos de Linux, Redes, Scripts e Docker para criar uma página web simples que monitora a conectividade de outros sites.

**Cenário**: Você precisa subir um contêiner Nginx que sirva um arquivo de texto simples contendo o status de conectividade de alguns sites, gerado automaticamente por um script Bash.

**Passo a passo do desafio**:

* **Python:** Crie um script em Python (`monitor.py`) utilizando a biblioteca `requests` para testar os sites. O desafio aqui é entender como gerenciar dependências de bibliotecas externas dentro de um container Docker (usando `pip install`).
* **Processamento de texto:** O script deve salvar o resultado desses testes formatado dentro de um arquivo chamado `status.txt` (ex: `Google: Online`, `SiteFalso: Offline`). Lembre-se de dar as permissões de execução (`chmod +x`) ao seu script.
* **Docker:** Crie um `Dockerfile` utilizando a imagem oficial do `nginx`. O seu Dockerfile deve copiar o arquivo `status.txt` para a pasta padrão que o Nginx usa (`/usr/share/nginx/html`).
* **Redes:** Faça o build da sua imagem (`docker build -t monitor-site .`) e rode o contêiner mapeando a porta `8080` do seu computador para a porta `80` do contêiner (`docker run -p 8080:80 monitor-site`).
* **Validação:** Abra o seu navegador e acesse [http://localhost:8080/status.txt](http://localhost:8080/status.txt) (ou use o comando `curl localhost:8080/status.txt` no terminal) para ver o relatório de conectividade gerado pelo seu script.
* **Bash**: Crie um único script chamado `deploy.sh` que executa o `monitor.py`, faz o `docker build` e o `docker run` de forma sequencial.

**Solução:** A solução para este desafio está [aqui](./solucao/), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

{% include next-steps.html
   prev_url="/content/modules/fundamentos/containers/"
   prev_title="Containers"
   next_url="/content/modules/cloud/"
   next_title="Cloud"
%}
