---
layout: default
title: Guia (Ferramentas locais)
permalink: /content/guides/ferramentas-locais/
---

# Guia: Ferramentas locais para os exercícios

Os laboratórios do Girus trazem o ambiente pronto, mas os **exercícios práticos** de cada módulo rodam direto no seu terminal e precisam de algumas ferramentas instaladas no seu computador. Este guia mostra como instalar e testar cada uma delas.

Você não precisa instalar tudo de uma vez: cada exercício lista as ferramentas que usa logo no início, com um link para a seção correspondente deste guia.

| Exercício | Ferramentas |
| --- | --- |
| Fundamentos | Docker |
| Cloud | Nenhuma (usa o Girus) |
| Pipeline | Git |
| Orquestração | Git, Docker, kubectl, Minikube |
| Observabilidade | Docker, kubectl, Minikube, Helm |
| Plataforma | Git, Docker, kubectl, Minikube, Node.js (npx) e Yarn |

> **Usuários de Windows:** instale o [WSL]({{ '/content/modules/introducao/preparacao-ambiente/#configuração-do-terminal' | relative_url }}) com Ubuntu e siga as instruções de **Linux** dentro dele. A única exceção é o Docker, explicado na seção abaixo.
>
> **Já instalou o Girus?** Ele também usa Docker e Kubernetes, então algumas dessas ferramentas podem já estar no seu computador. Rode o comando de verificação de cada seção antes de instalar.

Os comandos de Linux abaixo são para distribuições baseadas em Debian/Ubuntu (incluindo o WSL) em processadores Intel/AMD (`amd64`). No macOS, os comandos usam o [Homebrew](https://brew.sh).

---

## Git

O Git versiona o seu código, e os exercícios usam repositórios no GitHub para guardar os arquivos e acionar pipelines.

**Linux / WSL:**

```bash
sudo apt update
sudo apt install -y git
```

**macOS:**

```bash
brew install git
```

Depois de instalar, configure o seu nome e e-mail (eles aparecem em cada *commit*):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

Para enviar código ao GitHub (`git push`), você precisa se autenticar. O jeito mais simples é instalar o [GitHub CLI](https://cli.github.com/) e rodar `gh auth login`, que configura tudo por você.

**Verifique a instalação:**

```bash
git --version
```

---

## Docker

O Docker cria e executa contêineres. Ele também é a base do Minikube, que roda o cluster Kubernetes dentro de um contêiner.

**Windows e macOS:** instale o **Docker Desktop** pelo [site oficial do Docker](https://docs.docker.com/get-started/get-docker/). No Windows, abra o Docker Desktop, vá em *Settings* > *Resources* > *WSL Integration* e habilite a sua distribuição (ex: Ubuntu) para usar o comando `docker` dentro do WSL.

**Linux:** use o script oficial de instalação:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm get-docker.sh
```

Para rodar o `docker` sem precisar de `sudo`, adicione o seu usuário ao grupo `docker` e depois **feche e abra o terminal** (ou faça logout e login):

```bash
sudo usermod -aG docker $USER
```

**Verifique a instalação:**

```bash
docker run hello-world
```

Se aparecer a mensagem *"Hello from Docker!"*, está tudo certo.

---

## kubectl

O `kubectl` é a linha de comando do Kubernetes: é com ele que você cria, consulta e apaga recursos no cluster.

**Linux / WSL:**

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
rm kubectl
```

**macOS:**

```bash
brew install kubectl
```

**Verifique a instalação:**

```bash
kubectl version --client
```

Outras formas de instalação estão na [documentação oficial do Kubernetes](https://kubernetes.io/pt-br/docs/tasks/tools/).

---

## Minikube

O Minikube roda um cluster Kubernetes completo na sua máquina, para você estudar e errar de graça, sem criar nada na nuvem. Ele precisa do [Docker](#docker) instalado e em execução.

**Linux / WSL:**

```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64
```

**macOS:**

```bash
brew install minikube
```

**Suba o cluster e verifique:**

```bash
minikube start
kubectl get nodes
```

O comando `kubectl get nodes` deve listar um nó chamado `minikube` com o status `Ready`.

Os exercícios de Observabilidade e Plataforma sobem várias aplicações ao mesmo tempo. Se a sua máquina permitir, crie o cluster com mais recursos (os valores só são aplicados na **criação** do cluster; se ele já existe, apague-o antes com `minikube delete`):

```bash
minikube start --cpus 4 --memory 8g
```

**Quando terminar de estudar**, libere os recursos do seu computador:

```bash
minikube stop    # pausa o cluster, mantendo o que você instalou
minikube delete  # apaga o cluster por completo
```

> As soluções dos exercícios também mostram os comandos para o **Kind** e o **k3d**, alternativas ao Minikube. Qualquer um deles funciona, mas o roadmap usa o Minikube como padrão.

Mais detalhes na [documentação oficial do Minikube](https://minikube.sigs.k8s.io/docs/start/).

---

## Helm

O Helm é o gerenciador de pacotes do Kubernetes: com um comando, ele instala aplicações completas (como Prometheus e Grafana) no seu cluster.

**Linux / WSL:**

```bash
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-4 | bash
```

**macOS:**

```bash
brew install helm
```

**Verifique a instalação:**

```bash
helm version
```

Outras formas de instalação estão na [documentação oficial do Helm](https://helm.sh/pt/docs/intro/install).

---

## Node.js, npx e Yarn

O exercício de Plataforma gera um projeto do Backstage com o `npx` e faz o build com o `yarn`. Siga o [guia de instalação do Node.js, npx e Yarn]({{ '/content/guides/npx/' | relative_url }}).
