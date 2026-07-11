---
layout: default
title: Plataforma (Desafio)
---

# 6. Plataforma (Platform Engineering)

A Engenharia de Plataforma é a evolução do DevOps: construindo produtos IDPs (Internal Developer Portals) que oferecem autonomia, autoatendimento e padronização para desenvolvedores, reduzindo a carga cognitiva e acelerando o *time-to-market*.

## Desafio Prático (Plataforma)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para reforçar o conhecimento.

**Objetivo**: Construir a sua própria imagem do Backstage e instalá-la num cluster Kubernetes local, orquestrando na mão os múltiplos componentes (banco de dados, secrets, storage e a aplicação) que compõem um IDP real, e modelar o catálogo de software com as entidades Component, System, Resource, Domain, Group e User, entendendo como o Backstage representa relações de software e organização.

**Cenário**: Sua empresa decidiu adotar o Backstage como plataforma interna para desenvolvedores. Antes de propor a ferramenta em produção, você precisa validar a instalação e entender como as peças se conectam, provisionando um ambiente de testes local — e a sua própria imagem, não uma pronta de terceiros, para ter controle total sobre a configuração.

**Passo a passo do desafio:**

**Parte 1 — Build e instalação** (guia oficial: [Deploying with Kubernetes](https://backstage.io/docs/deployment/k8s/)):

1. Gere um projeto Backstage com `npx @backstage/create-app@latest`.
2. Faça o build de produção (`yarn install`, `yarn tsc`, `yarn build:backend`) e construa a imagem Docker a partir do `Dockerfile` gerado.
3. Publique a imagem num registry (ex: Docker Hub).
4. Inicie um cluster local (Minikube, Kind ou k3d) e crie um namespace dedicado para isolar o Backstage.
5. Provisione um PostgreSQL (Secret com as credenciais, armazenamento persistente e Deployment) para servir de banco de dados do Backstage.
6. Gere um GitHub PAT (Personal Access Token) com os escopos `repo` e `workflow`, para o Backstage acessar seus repositórios.
7. Crie o Deployment e o Service do Backstage usando a imagem que você publicou, conectando-o ao PostgreSQL e ao GitHub Token via variáveis de ambiente.
8. Acesse o painel via `port-forward` e confirme que a interface carrega em `http://localhost:7000`.

**Parte 2 — Catálogo** (guia oficial: [Software Catalog](https://backstage.io/docs/features/software-catalog/configuration)):

9. Publique o `catalog-info.yaml` (já gerado pelo `create-app`) no seu repositório do GitHub, e registre-o no catálogo do Backstage (**Create** -> **Register Existing Component**).
10. Expanda o `catalog-info.yaml` para modelar o ambiente: crie um `System` que agrupe os componentes, um `Resource` representando o PostgreSQL (com uma dependência `dependsOn` do componente do Backstage para esse Resource), um `Component` representando o Nginx do desafio de Orquestração associado ao mesmo System, um `Domain` que agrupe o System, e um `Group`/`User` representando o time responsável, usado como `owner` das demais entidades.

**Parte 3 — Bônus (opcional, avançado)** (guia oficial: [Authentication](https://backstage.io/docs/auth/)):

11. Crie um GitHub OAuth App e configure um provider de login real (SSO), editando o código-fonte do Backstage para adicionar o GitHub à tela de login.

**Solução:** A solução para este desafio está [aqui](./solution/), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

<p><span class="coming-soon-badge"><i class="fas fa-hammer"></i> Em breve: mais desafios para Backstage estão sendo construídos. Fique atento às novidades.</span></p>

{% include next-steps.html
   prev_url="/content/modules/plataforma/backstage/"
   prev_title="Backstage"
%}
