# Solução do Desafio: Pipeline (Módulo 3)

Este diretório contém a solução do desafio prático do módulo Pipeline. O objetivo deste projeto é unir **Terraform e GitHub Actions** em um fluxo simples que simula um processo real de Integração Contínua (CI) e validação de qualidade de código.

## Arquivos do Projeto

- **`main.tf`**: O código de infraestrutura básico contendo a declaração de recursos da AWS, criado especificamente para ser testado.
- **`.github/workflows/ci-terraform.yml`**: O arquivo do workflow do GitHub Actions. É ele que instrui o GitHub a preparar uma máquina virtual, instalar o Terraform e rodar as validações automaticamente.

## Como executar esta solução

Como o GitHub Actions roda na nuvem, você não executará um script localmente. Siga os passos abaixo:

### 1. Envie os arquivos para o GitHub

No seu terminal, crie um novo repositório para este desafio, certifique-se de estar na raiz do seu repositório local contendo a pasta `.github` e o arquivo `main.tf`. Adicione os arquivos e faça o push para a branch principal.

```bash
git add .
git commit -m "feat: adiciona pipeline de CI do terraform"
git push origin main
```

Como o GitHub Actions roda na nuvem, você não executará um script localmente. Siga os passos abaixo:

### 2. Acompanhe a execução

Acesse o seu repositório no site do GitHub e clique na aba "**Actions**" no menu superior. Você verá o seu workflow (Terraform CI) listado e rodando automaticamente.

### 3. Valide o resultado (Teste de Falha)

Se tudo ocorreu bem, os passos do pipeline ficarão com um ícone verde (sucesso).

Para ver o real poder da automação, faça um teste de falha:

1. Abra o arquivo `main.tf` na sua máquina e bagunce o código (apague uma chave `}`, tire a indentação ou digite um comando inválido).
2. Faça um novo commit e envie para o GitHub.
3. Volte na aba "**Actions**". Você verá o pipeline falhar (vermelho) nos passos de formatação ou validação, impedindo que o código quebrado seja aceito!

### Limpando o ambiente

Como este pipeline executa apenas etapas de validação e verificação (`terraform init`, `fmt -check` e `validate`), ele não cria recursos reais na sua conta da AWS. Portanto, não há o que ser destruído ou limpo para evitar custos.

Para deixar o seu repositório organizado novamente, basta corrigir o erro inserido no `main.tf` e fazer um novo push para que o pipeline volte a ficar verde:

```bash
git commit -am "fix: corrige sintaxe do terraform"
git push origin main
```

### Resumo do Aprendizado

Neste desafio, você praticou a base da cultura DevOps aplicada à infraestrutura (Shift-Left): automatizou a esteira de validação usando o GitHub Actions para garantir que nenhum código fora do padrão da equipe ou com erros estruturais do Terraform chegue ao ambiente de produção.
