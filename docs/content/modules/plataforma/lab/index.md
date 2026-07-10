---
layout: default
title: Plataforma (Desafio)
---

# 6. Plataforma (Platform Engineering)

A Engenharia de Plataforma é a evolução do DevOps: construindo produtos IDPs (Internal Developer Portals) que oferecem autonomia, autoatendimento e padronização para desenvolvedores, reduzindo a carga cognitiva e acelerando o *time-to-market*.

## Desafio Prático (Plataforma)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para reforçar o conhecimento.

**Objetivo**: Instalar a sua própria instância de Backstage num cluster Kubernetes local, orquestrando na mão os múltiplos componentes (banco de dados, secrets, storage e a aplicação) que compõem um IDP real.

**Cenário**: Sua empresa decidiu adotar o Backstage como plataforma interna para desenvolvedores. Antes de propor a ferramenta em produção, você precisa validar a instalação e entender como as peças se conectam, provisionando um ambiente de testes local.

**Passo a passo do desafio:**

1. Inicie um cluster local (Minikube, Kind ou k3d).
2. Crie um namespace dedicado para isolar o Backstage no cluster.
3. Provisione um PostgreSQL (Secret com as credenciais, armazenamento persistente e Deployment) para servir de banco de dados do Backstage.
4. Gere um GitHub PAT (Personal Access Token) com os escopos `repo` e `workflow`, para o Backstage acessar seus repositórios.
5. Crie o Deployment e o Service do Backstage, conectando-o ao PostgreSQL e ao GitHub Token via variáveis de ambiente.
6. Acesse o painel via `port-forward` e confirme que a interface carrega em `http://localhost:7000`.

**Solução:** A solução para este desafio está [aqui](./solution/installation/), mas consulte somente se não conseguir resolver por si só. Este guia de instalação é baseado no **guia oficial** [Deploying with Kubernetes](https://backstage.io/docs/deployment/k8s/).

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

<p><span class="coming-soon-badge"><i class="fas fa-hammer"></i> Em breve: mais desafios para Backstage estão sendo construídos. Fique atento às novidades.</span></p>

{% include next-steps.html
   prev_url="/content/modules/plataforma/backstage/"
   prev_title="Backstage"
%}
