# Ativando autenticação no Backstage

## 1. Criar o OAuth no GitHub

Acesse sua conta do Github e siga os passos:

1. Vá em **Settings** -> **Developer Settings** -> **OAuth Apps** -> **New OAuth Apps**.
2. Preencha as informações:
    - **Application name:** <http://localhost:7000>
    - **Authorization callback URL:** <http://localhost:7007/api/auth/github/handler/frame>

Edite o arquivo `backstage-secrets.yaml` e adicione os valores de `GITHUB_CLIENT_ID` e `GITHUB_CLIENT_SECRET`. Após isso, aplique as alterações:

```bash
kubectl apply -f backstage-secrets.yaml
```

## 2. Atualizar o `app-config.yaml`

No arquivo `app-config.yaml`, altere os valores de `auth.providers.github.development.clientId` e `auth.providers.github.development.clientSecret` pelos valores gerados no OAuth do GitHub.

## 3. Criar uma imagem Docker

Para essa configuração, vamos alterar o `app-config.yaml`, que é um arquivo de configuração do Backstage que é *buildado* junto da imagem.

Na instalação, esse passo foi pulado para simplificar, mas agora iremos executá-lo para fins de aprendizagem.

Faça o build da imagem:

```bash
eval $(minikube docker-env)
docker build -f Dockerfile -t backstage:1.0.0 .
```

TODO: continuar



## 1. Crie o configMap

Crie o `configMap` e atualize o `deployment` para "montar" as variáveis no Deployment.

```bash
kubectl apply -f backstage.yaml
```
