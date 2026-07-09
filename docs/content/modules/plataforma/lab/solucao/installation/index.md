---
layout: default
title: Plataforma (Desafio - Instalação do Backstage)
---

# Cloud Engineer Roadmap (DevOps/SRE/Platform)

Um guia de estudos para iniciantes de Cloud Engineer (DevOps/SRE/Platform) **gratuitos** e em **português**, com **laboratórios** e **desafios** para você evoluir a cada etapa.

---

## 6. Plataforma (Platform Engineering)

A Engenharia de Plataforma é a evolução do DevOps: construindo produtos IDPs (Internal Developer Portals) que oferecem autonomia, autoatendimento e padronização para desenvolvedores, reduzindo a carga cognitiva e acelerando o *time-to-market*.

## Instalando o Backstage no Kubernetes

Este guia de instalação é baseado no **guia oficial** [Deploying with Kubernetes](https://backstage.io/docs/deployment/k8s/).

### 1. Criar o namespace

Usaremos esse namespace para isolar o Backstage no nosso cluster Kubernetes. Crie o arquivo `namespace.yaml`.

```yaml
{% include_relative namespace.yaml %}
```

```bash
kubectl apply -f namespace.yaml -n backstage
```

### 2. Instalar o PostgreSQL

Crie o arquivo `postgres.yaml`, que define a secret com as credenciais, o armazenamento persistente e o deployment do PostgreSQL.

```yaml
{% include_relative postgres.yaml %}
```

```bash
kubectl apply -f postgres.yaml -n backstage
```

#### Verifique a conectividade do Pod

Verifique se o Pod do PostgreSQL está funcionando corretamente antes de seguir.

```bash
POSTGRESQL_PODNAME=$(kubectl get pods -l app=postgres -o jsonpath='{.items[0].metadata.name}')
kubectl exec -it --namespace=backstage $POSTGRESQL_PODNAME -- /bin/bash
```

Dentro do container, execute:

```bash
psql -U $POSTGRES_USER
```

Se o terminal abrir a linha de comando do PostgreSQL, quer dizer que funcionou. Use `CTRL + D` ou digite `exit` para sair do PostgreSQL e do container.

#### Instalar o Service do PostgreSQL

Crie o arquivo `postgres-service.yaml`.

```yaml
{% include_relative postgres-service.yaml %}
```

```bash
kubectl apply -f postgres-service.yaml
```

### 3. Instalar o Backstage

#### Criar o GITHUB_TOKEN

Crie um PAT (Personal Access Token) no GitHub para o Backstage ter acesso aos seus repositórios e workflows.

1. Acesse sua conta do GitHub e vá em **Settings** -> **Developer Settings** -> **Personal access tokens** -> **Tokens (classic)**.
2. Clique em **Generate new token (classic)**.
3. **Scopes (permissões):** marque `repo` (para ler e escrever repositórios) e `workflow` (para configurar as ações de CI automaticamente).
4. Copie o valor gerado (ex: `ghp_xxxxxxxxxxxxxxxxxxxxxxx`). Este é o seu `GITHUB_TOKEN`.

Crie o arquivo `backstage-secrets.yaml` e substitua o valor de `GITHUB_TOKEN` pelo token gerado.

```yaml
{% include_relative backstage-secrets.yaml %}
```

```bash
kubectl apply -f backstage-secrets.yaml
```

#### Criar o Deployment e o Service do Backstage

Crie o arquivo `backstage.yaml`.

```yaml
{% include_relative backstage.yaml %}
```

```bash
kubectl apply -f backstage.yaml
```

### 4. Acessar o painel

Como o Kubernetes já expõe um Service para o Backstage, basta redirecionar a porta para acessar no seu navegador:

```bash
kubectl port-forward svc/backstage 7000:80 -n backstage
```

> Acesse [http://localhost:7000](http://localhost:7000).

## Resumo do Aprendizado

Neste desafio, você instalou a sua primeira instância de um IDP (Internal Developer Portal). Você viu como orquestrar múltiplos componentes no Kubernetes (banco de dados, secrets, storage e a própria aplicação) e como integrar uma ferramenta de plataforma com o GitHub através de um token de acesso.

{% include next-steps.html
   prev_url="/content/modules/plataforma/lab/"
   prev_title="Desafio (Plataforma)"
%}
