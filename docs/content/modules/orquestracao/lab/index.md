---
layout: default
title: Orquestração (Desafio)
---

# 4. Orquestração

Orquestração de contêiner é o termo utilizado para o gerenciamento automatizado do ciclo de vida, escalabilidade e resiliência de dezenas ou milhares de contêineres.

## Desafio Prático (Orquestração)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para reforçar o conhecimento.

**Objetivo**: Juntar os seus conhecimentos de Kubernetes, ArgoCD e GitOps e aplicá-los num ambiente controlado (local), sem custos.

**Cenário**: O Nginx que criamos no Módulo 1 cresceu e agora precisa de alta disponibilidade. A sua missão é usar o **Minikube** (ferramenta usada para criar e testar os desafios) para rodar um cluster local, instalar o **ArgoCD** nele e fazer com que o ArgoCD leia um repositório no GitHub para fazer o deploy automático do seu site Nginx com 3 réplicas!

**Passo a passo do desafio:**

1. Inicie um cluster local usando o **Minikube**.
2. Crie um repositório público no GitHub (ex: `meu-deploy-gitops`) com um diretório `kubernetes/app`.
3. Dentro desse diretório, crie os manifestos do Kubernetes: um `namespace.yaml`, um `deployment.yaml` (usando a imagem `nginx:alpine` com 3 réplicas) e um `service.yaml` (do tipo NodePort).
4. Instale o ArgoCD no seu cluster local seguindo a [documentação oficial](https://argo-cd.readthedocs.io/en/stable/#quick-start).
5. Descubra a senha padrão do ArgoCD e faça um `port-forward` para acessar o painel dele no seu navegador (localhost).
6. No painel do ArgoCD, crie uma "New App" apontando para o seu repositório do GitHub.
7. Clique em *Sync* e veja que o ArgoCD vai ler os seus arquivos `.yaml` do GitHub e criar os Pods no seu computador!
8. Teste a resiliência criando um "drift" (desvio) ao apagar o Deployment manualmente usando o comando `kubectl delete deployment <nome-do-deployment> -n <namespace>` e veja que o ArgoCD irá recriá-lo automaticamente (certifique-se de habilitar as configurações corretas para isso acontecer).

**Solução:** A solução para este desafio está [aqui](./solution/), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

{% include next-steps.html
   prev_url="/content/modules/orquestracao/argocd/"
   prev_title="ArgoCD"
   next_url="/content/modules/observabilidade/"
   next_title="Observabilidade"
%}
