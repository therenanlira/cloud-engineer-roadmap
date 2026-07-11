---
layout: default
title: Orquestração (ArgoCD)
---

# 4. Orquestração

Orquestração de contêiner é o termo utilizado para o gerenciamento automatizado do ciclo de vida, escalabilidade e resiliência de dezenas ou milhares de contêineres.

## ArgoCD

ArgoCD é a ferramenta de GitOps mais popular. GitOps é o modelo de implantação contínua baseado no Git como única fonte de verdade. Com esse modelo, as mudanças em infraestrutura, como em Kubernetes, ocorrem via Git.
Por exemplo, mesmo que seja feita uma alteração manual no Kubernetes, o que chamamos de *drift* (desvio de configuração em comparação com o código da infraestrutura), as ferramentas de GitOps forçam a correção.

> Para os estudos e exercícios, **não crie um cluster na nuvem** (como EKS). Utilize ferramentas como **Minikube**. Elas rodam um cluster Kubernetes completo localmente na sua máquina, permitindo que você estude e erre de graça.

**Trilha de Estudo:**

* <i class="fas fa-video"></i> **Vídeo introdutório:** [[LinuxTips] Descomplicando o ArgoCD e o GitOps](https://youtu.be/TDvA2vAQCF8)
* <i class="fas fa-video"></i> **Vídeo aprofundado:** [[Fabricio Veronez] GitOps com ArgoCD na Prática: Do Zero ao Primeiro Deploy](https://youtu.be/NP0tWJh1XoE)

Com Kubernetes e ArgoCD, você já tem tudo que precisa para o exercício prático deste módulo.

{% include next-steps.html
   prev_url="/content/modules/orquestracao/kubernetes/"
   prev_title="Kubernetes & Helm"
   next_url="/content/modules/orquestracao/exercise/"
   next_title="Exercícios (Orquestração)"
%}
