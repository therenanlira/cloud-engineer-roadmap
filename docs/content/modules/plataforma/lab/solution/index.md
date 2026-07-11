---
layout: default
title: Plataforma (Desafio - Solução)
---

# 6. Plataforma (Platform Engineering)

A Engenharia de Plataforma é a evolução do DevOps: construindo produtos IDPs (Internal Developer Portals) que oferecem autonomia, autoatendimento e padronização para desenvolvedores, reduzindo a carga cognitiva e acelerando o *time-to-market*.

## Solução para o desafio prático (Plataforma)

Este guia é baseado no **guia oficial** [Deploying with Kubernetes](https://backstage.io/docs/deployment/k8s/), e constrói a sua própria imagem do Backstage, o que permite completar as 3 partes do desafio (instalar, criar catálogo e configurar SSO).

## Parte 1 — Build e instalação

### 1. Gere o projeto do Backstage

Crie um repositório no seu GitHub (ex: `meu-backstage`) e, na raiz do repositório, execute o comando:

```bash
npx @backstage/create-app@latest
```

> Se ainda não tiver instalado, siga o [guia de instalação de `npx`]({{ '/content/guides/npx/' | relative_url }}).

Quando for solicitado o nome do app, digite `meu-backstage`.

```bash
cd meu-backstage
```

### 2. Configure a integração com GitHub

O `app-config.yaml` gerado já vem com a integração do GitHub configurada por padrão (procure por `integrations.github`), usando a variável `GITHUB_TOKEN`. Não precisa editar nada aqui, só garantir que essa variável esteja definida quando o Backstage rodar (já cuidamos disso no Deployment mais abaixo).

### 3. Ajuste o `app-config.yaml`

Por padrão, o Backstage envia o cabeçalho `Content-Security-Policy` com a diretiva `upgrade-insecure-requests`, que instrui o navegador a forçar todas as conexões para HTTPS. Como este desafio roda tudo em `http://localhost`, sem TLS, o **Safari respeita essa diretiva à risca e tenta forçar HTTPS mesmo assim** — o que faz a página não carregar (o Chrome, por sua vez, ignora essa diretiva para `localhost`, então funciona sem esse ajuste).

Edite `app-config.yaml` e desative essa diretiva na seção `backend.csp`:

```yaml
backend:
  csp:
    connect-src: ["'self'", 'http:', 'https:']
    upgrade-insecure-requests: false
```

Aproveite e já ajuste a seção `catalog.rules` do mesmo arquivo: por padrão, ela só permite os tipos `Component, System, API, Resource, Location`. Na **Parte 2**, vamos modelar também `Domain`, `Group` e `User` — e, se algum desses tipos não estiver na lista, o Backstage rejeita o arquivo `catalog-info.yaml` **inteiro** (não só a entidade não permitida). Adicione os três tipos agora para não precisar rebuildar a imagem depois:

```yaml
catalog:
  rules:
    - allow: [Component, System, API, Resource, Location, Domain, Group, User]
```

### 4. Faça o build de produção

```bash
yarn install
yarn tsc
yarn build:backend
```

### 5. Construa a imagem Docker

```bash
docker image build . -f packages/backend/Dockerfile --tag <seu-usuario-dockerhub>/meu-backstage:latest
```

### 6. Publique no Docker Hub

```bash
docker login
docker push <seu-usuario-dockerhub>/meu-backstage:latest
```

### 7. Crie a estrutura de diretórios dos manifestos

Crie um repositório no seu GitHub (ex: `meu-backstage-infra`), e a estrutura `kubernetes/backstage`:

```bash
mkdir -p kubernetes/backstage
```

### 8. Criar o namespace

Dentro do diretório `kubernetes/backstage`, crie o arquivo `namespace.yaml`. Usaremos esse namespace para isolar o Backstage no nosso cluster Kubernetes.

```yaml
{% include_relative namespace.yaml %}
```

```bash
kubectl apply -f kubernetes/backstage/namespace.yaml -n backstage
```

### 9. Instalar o PostgreSQL

Escolha um usuário e uma senha para o banco e crie a secret direto via `kubectl`, em vez de escrevê-la num arquivo YAML. Assim o valor nunca vai parar num arquivo que possa ser commitado por engano, causando um vazamento de segredo:

```bash
kubectl create secret generic postgres-secrets \
  --namespace backstage \
  --from-literal=POSTGRES_USER='seu_usuario' \
  --from-literal=POSTGRES_PASSWORD='sua_senha'
```

> **Atenção:** use o valor **puro, sem base64** (`seu_usuario`, `sua_senha`). O `--from-literal` já faz a codificação em base64 sozinh. Se você mesmo rodar `echo -n "..." | base64` antes e colar o resultado aqui, o valor fica codificado **duas vezes**, e o Backstage não vai conseguir usá-lo.

Dentro do diretório `kubernetes/backstage`, crie o arquivo `postgres.yaml`. Este define o armazenamento persistente e o deployment do PostgreSQL (que consome a secret criada acima).

```yaml
{% include_relative postgres.yaml %}
```

```bash
kubectl apply -f kubernetes/backstage/postgres.yaml -n backstage
```

#### Verifique a conectividade do Pod

Verifique se o Pod do PostgreSQL está funcionando corretamente antes de seguir.

```bash
POSTGRESQL_PODNAME=$(kubectl get pods -n backstage -l app=postgres -o jsonpath='{.items[0].metadata.name}')
kubectl exec -it --namespace=backstage $POSTGRESQL_PODNAME -- /bin/bash
```

Dentro do container, execute:

```bash
psql -U $POSTGRES_USER
```

Se o terminal abrir a linha de comando do PostgreSQL, quer dizer que funcionou. Use `CTRL + D` ou digite `exit` para sair do PostgreSQL e do container.

#### Instalar o Service do PostgreSQL

Dentro do diretório `kubernetes/backstage`, crie o arquivo `postgres-service.yaml`.

```yaml
{% include_relative postgres-service.yaml %}
```

```bash
kubectl apply -f kubernetes/backstage/postgres-service.yaml
```

### 10. Criar o GITHUB_TOKEN

Crie um PAT (Personal Access Token) no GitHub para o Backstage ter acesso aos seus repositórios e workflows.

> Esse token serve para a **integração de catálogo** (o Backstage ler seus repositórios e arquivos `catalog-info.yaml`).

1. Acesse sua conta do GitHub e vá em **Settings** -> **Developer Settings** -> **Personal access tokens** -> **Tokens (classic)**.
2. Clique em **Generate new token (classic)**.
3. **Scopes (permissões):** marque `repo` (para ler e escrever repositórios) e `workflow` (para configurar as ações de CI automaticamente).
4. Copie o valor gerado (ex: `ghp_xxxxxxxxxxxxxxxxxxxxxxx`). Este é o seu `GITHUB_TOKEN`.

Pelo mesmo motivo do passo anterior, crie a secret direto via `kubectl`, sem escrevê-la num arquivo. Use o `ghp_...` **direto, sem passar por base64** — o `--from-literal` já faz isso sozinho:

```bash
kubectl create secret generic backstage-secrets \
  --namespace backstage \
  --from-literal=GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxxxxx'
```

### 11. Criar o Deployment e o Service do Backstage

Dentro do diretório `kubernetes/backstage`, crie o arquivo `backstage.yaml`. Troque `<seu-usuario-dockerhub>` pela imagem que você publicou no passo 5.

```yaml
{% include_relative backstage.yaml %}
```

```bash
kubectl apply -f kubernetes/backstage/backstage.yaml
```

### 12. Acessar o painel

```bash
kubectl port-forward svc/backstage 7000:80 -n backstage
```

> Acesse [http://localhost:7000](http://localhost:7000). Clique em **Guest** -> **ENTER** para entrar.

## Parte 2 — Catálogo

Após instalar o Backstage, siga para a configuração do catálogo de software. O próprio `create-app` já gerou um arquivo `catalog-info.yaml` na raiz do seu projeto `meu-backstage`, descrevendo a própria aplicação.

Faça o commit e o push desse arquivo (junto com o resto do código do `meu-backstage`) para um repositório no seu GitHub:

```bash
git add .
git commit -m "feat: cria o app meu-backstage"
git push -u origin main
```

De volta ao painel do Backstage, clique no ícone **+** (**Create**) no menu lateral e depois em **Register Existing Component**. Cole a URL **do arquivo** (ex: `https://github.com/<seu-usuario>/meu-backstage/blob/main/catalog-info.yaml`) — **não** a URL do repositório — e clique em **ANALYZE**.

> Colar só a URL do repositório (sem o caminho até o arquivo) ativa um modo diferente do assistente, que varre o repositório inteiro e, se não encontrar o `catalog-info.yaml` de primeira, pede para você fazer login com o GitHub para confirmar o *owner* do componente. Esse login só funciona depois de configurado o provider de SSO na **Parte 3** — por isso, use sempre a URL completa até o arquivo.

Se tudo correu bem, o Backstage vai encontrar o componente `meu-backstage` e permitir importá-lo. Depois de importado, ele aparece na página **Catalog**.

> **Erro 401 Unauthorized ao analisar o arquivo?** O `GITHUB_TOKEN` só é lido pelo Backstage quando o Pod *inicia* — se você criou ou recriou a secret `backstage-secrets` depois que o Deployment já estava rodando, reinicie-o para o valor novo ser aplicado:
>
> ```bash
> kubectl rollout restart deployment/backstage -n backstage
> ```
>
> Se o erro persistir, teste o token isoladamente (fora do Kubernetes) para descartar um token expirado ou sem permissão:
>
> ```bash
> curl -H "Authorization: token SEU_TOKEN_AQUI" https://api.github.com/repos/<seu-usuario>/meu-backstage/contents/catalog-info.yaml
> ```

### Modele o catálogo: Component, System, Resource, Domain, Group e User

Um catálogo de software raramente descreve componentes isolados. Ele organiza componentes relacionados sob um **System**, agrupa Systems relacionados sob um **Domain** (uma área de negócio ou produto), modela dependências externas como um **Resource** (ex: um banco de dados), e representa a estrutura organizacional com **Group** e **User** — usados como `owner` das demais entidades. Vamos expandir o `catalog-info.yaml` para refletir o que você de fato provisionou neste desafio, com essas seis entidades.

Edite o `catalog-info.yaml` na raiz do `meu-backstage` para o seguinte conteúdo (troque `<seu-usuario-github>` pelo seu usuário):

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: meu-backstage
  description: An example of a Backstage application.
spec:
  type: website
  owner: group:time-plataforma
  lifecycle: experimental
  system: plataforma-devops
  dependsOn:
    - resource:postgres
---
apiVersion: backstage.io/v1alpha1
kind: System
metadata:
  name: plataforma-devops
  description: Agrupa os componentes provisionados no desafio de Plataforma.
spec:
  owner: group:time-plataforma
  domain: developer-experience
---
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: postgres
  description: Banco de dados PostgreSQL que armazena os dados do catálogo do Backstage.
spec:
  type: database
  owner: group:time-plataforma
  system: plataforma-devops
---
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: meu-site-nginx
  description: Servidor Nginx provisionado no desafio de Orquestração.
spec:
  type: service
  owner: group:time-plataforma
  lifecycle: production
  system: plataforma-devops
---
apiVersion: backstage.io/v1alpha1
kind: Domain
metadata:
  name: developer-experience
  description: Domínio de plataformas internas e ferramentas para desenvolvedores.
spec:
  owner: group:time-plataforma
---
apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: time-plataforma
  description: Time responsável por operar o IDP.
spec:
  type: team
  children: []
---
apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: <seu-usuario-github>
spec:
  memberOf: [time-plataforma]
```

> Um único arquivo pode descrever **várias entidades**, separadas por `---` — é assim que o próprio Backstage organiza seus dados de exemplo internos (um System, um Component e uma API, todos no mesmo arquivo).

Note que o `meu-site-nginx` não tem código-fonte dentro do repositório `meu-backstage`, ele representa um serviço que já existe no seu cluster (o Nginx provisionado no desafio de Orquestração). Isso é normal: o catálogo modela toda a paisagem de software da empresa, não apenas o conteúdo do repositório atual.

> **Erro "is not of an allowed kind for that location"?** Isso significa que o `catalog.rules` do `app-config.yaml` não inclui `Domain`, `Group` e `User` — volte ao [passo 3 da Parte 1](#3-ajuste-o-app-configyaml) e confirme o ajuste. Sem ele, o Backstage rejeita o arquivo **inteiro** (nenhuma das entidades é registrada, nem as que já eram permitidas antes), então é preciso reconstruir e republicar a imagem para o ajuste ter efeito.

Faça o commit e o push da mudança:

```bash
git add catalog-info.yaml
git commit -m "feat: modela Component, System, Resource, Domain, Group e User no catálogo"
git push
```

Como o arquivo já está registrado como *location* no catálogo, não é preciso repetir o **Register Existing Component**. Abra a página do componente `meu-backstage`, e clique no ícone de **Refresh** (ao lado do nome, no topo) para forçar a releitura imediata do arquivo — ou aguarde a atualização automática periódica do Backstage.

Depois do refresh, acesse o menu **Catalog**, filtre por **Kind: System**, e abra o `plataforma-devops`: ele deve agrupar os dois componentes e o Resource, e mostrar o `developer-experience` como Domain. Na aba **Diagram** dessa página, você vê visualmente a dependência (`dependsOn`) do `meu-backstage` com o Resource `postgres`. Filtrando por **Kind: Group**, o `time-plataforma` aparece como owner de todas as entidades que você criou.

## Parte 3 — Bônus (Avançado): Login via GitHub (SSO)

Por padrão, a tela de login do Backstage só oferece a opção **Guest**. Como agora você tem o código-fonte do próprio app, dá pra adicionar um provider de verdade.

### 1. Crie um GitHub OAuth App

Em **Settings** -> **Developer settings** -> **OAuth Apps** -> **New OAuth App**:

* **Homepage URL:** `http://localhost:7000`
* **Authorization callback URL:** `http://localhost:7000/api/auth/github/handler/frame`

Isso gera um **Client ID** e um **Client Secret**.

### 2. Configure o backend

Edite `packages/backend/src/index.ts` e registre o módulo do provider do GitHub, logo abaixo do `guest-provider`:

```ts
backend.add(import('@backstage/plugin-auth-backend-module-guest-provider'));
backend.add(import('@backstage/plugin-auth-backend-module-github-provider'));
```

### 3. Adicione a tela de login com o GitHub

Crie o arquivo `packages/app/src/modules/sign-in/index.tsx`:

```tsx
import { createFrontendModule } from '@backstage/frontend-plugin-api';
import { SignInPageBlueprint } from '@backstage/plugin-app-react';
import { SignInPage } from '@backstage/core-components';
import { githubAuthApiRef } from '@backstage/core-plugin-api';

const githubSignInPage = SignInPageBlueprint.make({
  params: {
    loader: async () => props => (
      <SignInPage
        {...props}
        auto
        providers={[
          'guest',
          {
            id: 'github-auth-provider',
            title: 'GitHub',
            message: 'Sign in using GitHub',
            apiRef: githubAuthApiRef,
          },
        ]}
      />
    ),
  },
});

export const signInModule = createFrontendModule({
  pluginId: 'app',
  extensions: [githubSignInPage],
});
```

E registre esse módulo em `packages/app/src/App.tsx`:

```tsx
import { createApp } from '@backstage/frontend-defaults';
import catalogPlugin from '@backstage/plugin-catalog/alpha';
import { navModule } from './modules/nav';
import { signInModule } from './modules/sign-in';

export default createApp({
  features: [catalogPlugin, navModule, signInModule],
});
```

### 4. Adicione as credenciais do OAuth App

A secret `backstage-secrets` já existe (criada na Parte 1). Para adicionar as novas chaves sem escrever nenhum valor em disco, recrie-a com o Client ID e o Client Secret gerados no passo 1, além do `GITHUB_TOKEN` já usado — todos **sem base64**, como da primeira vez:

```bash
kubectl delete secret backstage-secrets -n backstage

kubectl create secret generic backstage-secrets \
  --namespace backstage \
  --from-literal=GITHUB_TOKEN='ghp_xxxxxxxxxxxxxxxxxxxxxxx' \
  --from-literal=AUTH_GITHUB_CLIENT_ID='seu_client_id' \
  --from-literal=AUTH_GITHUB_CLIENT_SECRET='seu_client_secret'
```

Adicione ao `backstage.yaml` as variáveis que apontam para essa secret:

```yaml
- name: APP_CONFIG_auth_providers_github_development_clientId
  valueFrom:
    secretKeyRef:
      name: backstage-secrets
      key: AUTH_GITHUB_CLIENT_ID
- name: APP_CONFIG_auth_providers_github_development_clientSecret
  valueFrom:
    secretKeyRef:
      name: backstage-secrets
      key: AUTH_GITHUB_CLIENT_SECRET
```

### 5. Rebuild, republique e reaplique

```bash
yarn build:backend
docker image build . -f packages/backend/Dockerfile --tag <seu-usuario-dockerhub>/meu-backstage:latest
docker push <seu-usuario-dockerhub>/meu-backstage:latest
kubectl rollout restart deployment/backstage -n backstage
```

Acesse `http://localhost:7000` novamente (numa aba anônima, para não reaproveitar a sessão de Guest) e confirme que agora aparece um card **GitHub** ao lado do **Guest**, com um botão **SIGN IN** que leva você para a tela de login do GitHub de verdade.

## Limpando o ambiente

Para liberar a memória e os recursos da sua máquina, delete o cluster após terminar os testes:

```bash
minikube delete
# ou
kind delete cluster
# ou
k3d cluster delete
```

## Resumo do Aprendizado

Neste desafio, você foi além de só instalar uma imagem pronta: construiu a sua própria imagem do Backstage a partir do zero, publicou num registry, orquestrou múltiplos componentes no Kubernetes (banco de dados, secrets, storage e a aplicação), teve o primeiro contato com o catálogo de software registrando um componente, e — por ter o controle do código-fonte — conseguiu configurar um provider de autenticação real via GitHub.

{% include next-steps.html
   prev_url="/content/modules/plataforma/lab/"
   prev_title="Desafio (Plataforma)"
%}
