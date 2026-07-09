# Solução do Desafio: Orquestração (Módulo 4)

Este diretório contém a solução do desafio prático de Orquestração. O objetivo deste projeto é montar o seu primeiro fluxo **GitOps** utilizando um cluster local e o **ArgoCD** para fazer o deploy automatizado de uma aplicação Nginx.

A grande vantagem desta abordagem é que o estado da sua infraestrutura passa a viver no GitHub. Se o seu cluster perder configurações críticas, basta apontar o ArgoCD para o GitHub novamente; ele reconstruirá tudo sozinho!

## 🗂️ Arquivos do Projeto

- **`deployment.yaml`**: O manifesto que instrui o Kubernetes a criar 3 réplicas (Pods) da nossa aplicação Nginx.
- **`service.yaml`**: O manifesto que cria um Serviço do tipo NodePort para podermos acessar o Nginx no nosso navegador.

*(Nota: Para este desafio funcionar, você deve fazer o push destes dois arquivos para a branch principal de um repositório público no seu próprio GitHub).*

## 🚀 Passo a Passo no Terminal

Com os arquivos devidamente enviados para o seu GitHub, abra o terminal local e siga os passos abaixo.

### 1. Inicie o cluster local

Escolha a sua ferramenta de preferência para subir o cluster:

```bash
# Opção A: Minikube
minikube start

# Opção B: Kind
kind create cluster

# Opção C: k3d
k3d cluster create
```

### 2. Instale o ArgoCD

Execute os comandos da documentação oficial para criar o namespace e instalar a ferramenta:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f [https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml](https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml)
```

### 3. Acesse a interface do ArgoCD

Aguarde os pods do ArgoCD estarem rodando. Depois, resgate a senha padrão e libere o acesso ao painel:

```bash
# Resgata a senha do usuário 'admin'
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

# Redireciona a porta para acessar o painel
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

> Abra no navegador: https://localhost:8080 (Ignore o aviso de segurança) e faça login com o usuário admin e a senha gerada.

### 4. Configure a Aplicação no ArgoCD

No painel do ArgoCD, clique em + NEW APP e preencha com os dados do seu repositório:

- Application Name: meu-site-gitops
- Project: default
- Sync Policy: Automatic (Essencial para o ArgoCD corrigir problemas sozinho).
- Sync Policy - Self-Heal: Ativado (Essencial para se recuperar de drifts)
- Repository URL: O link do seu repositório do GitHub contendo os YAMLs.
- Path: `.` (Ponto, para a raiz do repositório).
- Cluster URL: https://kubernetes.default.svc
- Namespace: default
- Clique em CREATE.

### Valide o Resultado (Teste de Resiliência)

Para ver a verdadeira mágica do GitOps, vamos simular um desastre. Vá ao seu terminal e delete o Deployment inteiro:

```bash
kubectl delete deployment meu-site-nginx
```

Olhe rapidamente para o painel do ArgoCD. Você verá que ele detectou que o cluster local está diferente do que está no GitHub (OutOfSync) e, como a política está Automática, ele recriará o Deployment imediatamente!

### Limpando o ambiente

Para liberar a memória e os recursos da sua máquina, delete o cluster após terminar os testes:

```bash
# Minikube:
minikube delete

# Kind:
kind delete cluster

# k3d:
k3d cluster delete
```

### Resumo do Aprendizado

Neste desafio, você testou o ápice da orquestração moderna. Em vez de aplicar arquivos manualmente (kubectl apply), delegou essa função ao ArgoCD. Ao tentar deletar o Deployment, você viu que não é mais possível alterar a infraestrutura permanentemente pelo terminal, pois o "desejo" da sua aplicação está protegido e versionado no GitHub. Isso é GitOps!
