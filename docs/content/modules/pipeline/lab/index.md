---
layout: default
title: Pipeline (Desafio)
---

# Cloud Engineer Roadmap (DevOps/SRE/Platform)

Um guia de estudos para iniciantes de Cloud Engineer (DevOps/SRE/Platform) **gratuitos** e em **português**, com **laboratórios** e **desafios** para você evoluir a cada etapa.

---

## 3. Pipeline

Pipelines são fluxos automatizados de integração (build) e entrega (deploy) contínua, também conhecido como CI/CD (Continuous Integration / Continuou Deployment).

### Desafio Prático (Pipeline)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para o reforçar o conhecimento.

**Objetivo:** Criar a sua primeiro pipeline de Integração Contínua (CI) usando GitHub Actions para validar a sua infraestrutura como código (Terraform) e garantir que ela não contenha erros de sintaxe ou formatação.

**Cenário:** Você precisa garantir que ninguém da equipe envie um código Terraform quebrado para o repositório. Para isso, a pipeline deve rodar automaticamente toda vez que houver um `push` na branch `main`.

**Passo a passo do desafio:**

1. Crie um repositório no seu GitHub.
2. Crie um arquivo `main.tf` simples na raiz do repositório contendo apenas a declaração do *provider* da AWS e um recurso básico (como uma VPC).
3. Crie a estrutura de diretórios obrigatória do GitHub Actions: `.github/workflows/`.
4. Dentro dessa pasta, crie um arquivo chamado `ci-terraform.yml`.
5. Escreva um workflow que:
   * Seja acionado em eventos de `push` e `pull_request` para a branch `main`.
   * Faça o *checkout* do seu código.
   * Configure o ambiente do Terraform (**Dica:** pesquise pela *Action* oficial `hashicorp/setup-terraform`).
   * Execute o comando `terraform init`.
   * Execute o comando `terraform fmt -check` (para garantir que o código segue o padrão de estilo).
   * Execute o comando `terraform validate` (para garantir que a sintaxe está correta).
6. Faça o *commit* propositalmente mal formatado para ver o pipeline falhar, corrija-o e veja o pipeline ficar verde (sucesso)!

**Solução:** A solução para este desafio está [aqui](./solucao/), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

{% include next-steps.html
   prev_url="/content/modules/pipeline/github-actions/"
   prev_title="GitHub Actions"
   next_url="/content/modules/orquestracao/"
   next_title="Orquestração"
%}
