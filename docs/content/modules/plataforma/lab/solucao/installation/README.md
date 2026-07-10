# Instalando o Backstage no Kubernetes

## 1. Criar o Namespace

Usaremos essa namespace para isolar o Backstage no nosso cluster Kubernetes.

```bash
kubectl apply -f namespace.yaml -n backstage
```

## 2. Instalar o PostgreSQL

Instalar as secrets, storage e o deployment do PostgreSQL.

Antes de aplicar, edite `postgres.yaml` e substitua `POSTGRES_USER` e `POSTGRES_PASSWORD` pelas versões em base64 do seu usuário e senha (o campo `data` do Kubernetes exige valores em base64):

```bash
echo -n "seu_usuario" | base64
echo -n "sua_senha" | base64
```

```bash
kubectl apply -f postgres.yaml -n backstage
```

### 1. Verificar a conectividade do Pod

Verifique se o Pod do PostgreSQL está funcionando corretamente antes de seguir.

```bash
POSTGRESQL_PODNAME=$(kubectl get pods -l app=postgres -o jsonpath='{.items[0].metadata.name}')
kubectl exec -it --namespace=backstage $POSTGRESQL_PODNAME -- /bin/bash
```

Dentro do container, execute:

```bash
psql -U $POSTGRES_USER
```

Se o terminal abrir o `command line` do PostgreSQL, quer dizer que funcionou.

Use `CTRL + D` ou digite `exit` para sair do PostgreSQL e do container.

### 2. Instalar o Service do PostgreSQL

```bash
kubectl apply -f postgres-service.yaml
```

## 3. Instalar o Backstage

### 1. Criar o GITHUB_TOKEN

Crie um PAT (Personal Access Token) no GitHub para o Backstage ter acesso aos seus repositórios e workflows do GitHub.

Acesse sua conta do Github e siga os passos:

1. Vá em **Settings** -> **Developer Settings** -> **Personal access tokens** -> **Tokens (classic)**.
2. Clique em **Generate new token (classic)**.
3. **Scopes (Permissões):** Marque as permissões de repo (para ler e escrever repositórios) e workflow (para configurar as ações de CI automaticamente).
4. Copie o valor gerado (ex: ghp_xxxxxxxxxxxxxxxxxxxxxxx). Este é o seu **GITHUB_TOKEN**.

Edite o arquivo `backstage-secrets.yaml` e substitua `GITHUB_TOKEN` pela versão em base64 do token gerado:

```bash
echo -n "ghp_xxxxxxxxxxxxxxxxxxxxxxx" | base64
```

```bash
kubectl apply -f backstage-secrets.yaml
```

### 2. Instalar o Backstage

```bash
kubectl apply -f backstage.yaml
```

### 3. Acessar o Painel

Como o Kubernetes já expõe um Service para o Backstage, basta redirecionar a porta para acessar no seu navegador:

```bash
kubectl port-forward svc/backstage 7000:80 -n backstage
```

> Acesse [http://localhost:7000](http://localhost:7000).
