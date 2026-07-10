---
layout: default
title: Orquestração (Desafio - Solução)
---

# 4. Orquestração

Orquestração de contêiner é o termo utilizado para o gerenciamento automatizado do ciclo de vida, escalabilidade e resiliência de dezenas ou milhares de contêineres.

## Solução para o desafio prático (Orquestração)

O objetivo deste desafio é montar o seu primeiro fluxo **GitOps** utilizando um cluster local e o **ArgoCD** para fazer o deploy automatizado de uma aplicação Nginx. A grande vantagem desta abordagem é que o estado da sua infraestrutura passa a viver no GitHub: se o seu cluster perder configurações críticas, basta apontar o ArgoCD para o GitHub novamente que ele reconstruirá tudo sozinho!

### 1. Manifestos do Kubernetes

Crie um repositório público no seu GitHub (ex: `meu-deploy-gitops`), e crie a estrutura de diretórios `kubernetes/app`.

```bash
mkdir -p kubernetes/app
```

Dentro do diretório `kubernetes/app`, crie os três manifestos abaixo.

#### `namespace.yaml`

Dentro do diretório `kubernetes/app`, crie o arquivo `namespace.yaml`, que instrui o Kubernetes a criar a namespace da nossa aplicação Nginx.

```yaml
{% include_relative namespace.yaml %}
```

#### `deployment.yaml`

Dentro do diretório `kubernetes/app`, crie o arquivo `deployment.yaml`, que instrui o Kubernetes a criar 3 réplicas (Pods) da nossa aplicação Nginx.

```yaml
{% include_relative deployment.yaml %}
```

#### `service.yaml`

Dentro do diretório `kubernetes/app`, crie o arquivo `service.yaml`, que cria um Serviço do tipo NodePort para podermos acessar o Nginx no navegador.

```yaml
{% include_relative service.yaml %}
```

Faça o commit e o push destes dois arquivos para a branch principal do seu repositório:

```bash
git add .
git commit -m "feat: adiciona manifestos do nginx"
git push origin main
```

### 2. Inicie o cluster local

Escolha a sua ferramenta de preferência para subir o cluster:

Minikube:

```bash
minikube start
```

Kind:

```bash
kind create cluster
```

k3d:

```bash
k3d cluster create "my-cluster-name"
```

### 3. Instale o ArgoCD

Execute os comandos da documentação oficial para criar o namespace e instalar a ferramenta:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### 4. Acesse a interface do ArgoCD

Aguarde os pods do ArgoCD estarem rodando. Depois, resgate a senha padrão e libere o acesso ao painel:

```bash
# Resgata a senha do usuário 'admin'
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

# Redireciona a porta para acessar o painel
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

> Abra no navegador `https://localhost:8080` (ignore o aviso de segurança) e faça login com o usuário `admin` e a senha gerada.

### 5. Configure a aplicação no ArgoCD

No painel do ArgoCD, clique em **+ NEW APP** e preencha com os dados do seu repositório:

* **Application Name:** `meu-site-gitops`
* **Project:** `default`
* **Sync Policy:** `Automatic` (essencial para o ArgoCD corrigir problemas sozinho)
* **Sync Policy - Self Heal:** ativado (essencial para se recuperar de drifts)
* **Sync Policy - Prune Resources:** ativado (essencial para deletar recursos quando os manifestos forem deletados)
* **Repository URL:** o link do seu repositório do GitHub contendo os YAMLs
* **Path:** `kubernetes/app`
* **Cluster URL:** `https://kubernetes.default.svc`
* **Namespace:** `app`

Clique em **CREATE**.

### 6. Valide o resultado (teste de resiliência)

Para ver o GitOps em ação, vamos simular um desastre. Vá ao seu terminal e delete o Deployment inteiro:

```bash
kubectl delete deployment meu-site-nginx
```

Olhe rapidamente para o painel do ArgoCD. Você verá que ele detectou que o cluster local está diferente do que está no GitHub (`OutOfSync`) e, como a política está automática, ele recriará o Deployment imediatamente!

## Limpando o ambiente

Para liberar a memória e os recursos da sua máquina, delete o cluster após terminar os testes:

Minikube:

```bash
minikube delete
```

Kind:

```bash
kind delete cluster
```

k3d:

```bash
k3d cluster delete
```

## Resumo do Aprendizado

Neste desafio, você testou GitOps na prática. Em vez de aplicar arquivos manualmente (`kubectl apply`), delegou essa função ao ArgoCD. Ao tentar deletar o Deployment, você viu que não é mais possível alterar a infraestrutura permanentemente pelo terminal, pois o estado desejado da sua aplicação está protegido e versionado no GitHub.

{% include next-steps.html
   prev_url="/content/modules/orquestracao/lab/"
   prev_title="Desafio (Orquestração)"
   next_url="/content/modules/observabilidade/"
   next_title="Observabilidade"
%}
