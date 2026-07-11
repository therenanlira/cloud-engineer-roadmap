---
layout: default
title: Pipeline (Exercício - Solução)
---

# 3. Pipeline

Pipelines são fluxos automatizados de integração (build) e entrega (deploy) contínua, também conhecidos como CI/CD (Continuous Integration / Continuous Deployment).

## Solução para o exercício prático (Pipeline)

O objetivo deste exercício é unir **Terraform e GitHub Actions** em um fluxo simples que simula um processo real de Integração Contínua (CI) e validação de qualidade de código.

### 1. Código Terraform

Crie um repositório no seu GitHub (ex: `minha-pipeline`), e crie o diretório `terraform`.

```bash
mkdir terraform
```

Dentro do diretório `terraform`, crie o arquivo `main.tf`.

```hcl
{% include_relative main.tf %}
```

### 2. Workflow do GitHub Actions

Crie a estrutura de diretórios `.github/workflows/`.

```bash
mkdir -p .github/workflows/
```

Dentro desta estrutura de diretórios, crie o arquivo `ci-terraform.yaml`. É ele que instrui o GitHub a preparar uma máquina virtual, instalar o Terraform e rodar as validações automaticamente.

```yaml
{% include_relative ci-terraform.yaml %}
```

### 3. Envie os arquivos para o GitHub

Como o GitHub Actions roda na nuvem, você não executará um script localmente. Certifique-se de estar na raiz do seu repositório local contendo a pasta `.github` e o arquivo `main.tf`, adicione os arquivos e faça o push para a branch principal.

```bash
git add .
git commit -m "feat: adiciona pipeline de CI do terraform"
git push origin main
```

### 4. Acompanhe a execução

Acesse o seu repositório no site do GitHub e clique na aba **Actions** no menu superior. Você verá o seu workflow (Terraform CI) listado e rodando automaticamente.

### 5. Valide o resultado (teste de falha)

Se tudo ocorreu bem, os passos do pipeline ficarão com um ícone verde (sucesso).

Para ver o real poder da automação, faça um teste de falha:

1. Abra o arquivo `main.tf` na sua máquina e bagunce o código (apague uma chave `}`, tire a indentação ou digite um comando inválido).
2. Faça um novo commit e envie para o GitHub.
3. Volte na aba **Actions**. Você verá o pipeline falhar (vermelho) nos passos de formatação ou validação, impedindo que o código quebrado seja aceito!

```bash
git commit -am "fix: corrige sintaxe do terraform"
git push origin main
```

## Limpando o ambiente

Como este pipeline executa apenas etapas de validação e verificação (`terraform init`, `fmt -check` e `validate`), ele não cria recursos reais na sua conta da AWS. Portanto, não há o que ser destruído ou limpo para evitar custos.

## Resumo do Aprendizado

Neste exercício, você praticou a base da cultura DevOps aplicada à infraestrutura (Shift-Left): automatizou a esteira de validação usando o GitHub Actions para garantir que nenhum código fora do padrão da equipe ou com erros estruturais do Terraform chegue ao ambiente de produção.

{% include next-steps.html
   prev_url="/content/modules/pipeline/lab/"
   prev_title="Exercício (Pipeline)"
   next_url="/content/modules/orquestracao/"
   next_title="Orquestração"
%}
