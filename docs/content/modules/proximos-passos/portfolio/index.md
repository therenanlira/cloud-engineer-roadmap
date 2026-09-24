---
layout: default
title: Próximos passos (Projetos para portfólio)
---

# Próximos passos

## Projetos para portfólio

Os exercícios do roadmap foram feitos para fixar cada módulo separadamente. Um projeto de portfólio vai além: junta vários módulos em um único repositório público, que qualquer recrutador ou pessoa entrevistadora consegue abrir e entender o que você sabe fazer.

Os projetos abaixo estão em ordem de dificuldade. Não é preciso fazer todos: um projeto bem feito e bem documentado vale mais do que vários incompletos.

### Projeto 1: Aplicação conteinerizada com pipeline de CI/CD

**Módulos:** Fundamentos, Pipeline.

1. Escolha (ou escreva) uma aplicação web simples, em qualquer linguagem, e crie um `Dockerfile` para ela.
2. Crie um workflow no GitHub Actions que, a cada *push*, rode os testes, faça o build da imagem e a publique no [GitHub Container Registry](https://docs.github.com/pt/packages/working-with-a-github-packages-registry/working-with-the-container-registry).
3. Adicione um *badge* de status do pipeline no `README.md`.

**Diferencial:** use tags de versão (ex: `v1.0.0`) para gerar imagens versionadas, e não só `latest`.

### Projeto 2: Infraestrutura na AWS com Terraform e CI/CD

**Módulos:** Cloud, Pipeline.

1. Com Terraform, provisione na AWS uma infraestrutura simples dentro da camada gratuita (ex: um site estático no S3 ou uma função Lambda).
2. Guarde o *state* do Terraform em um *backend* remoto (bucket S3).
3. Crie um pipeline que rode `terraform plan` a cada *Pull Request* e `terraform apply` somente depois do *merge* na `main`.
4. Use o [InfraCost](https://github.com/infracost/infracost) para mostrar no *Pull Request* quanto a mudança vai custar (FinOps na prática).

**Atenção:** crie um alerta de faturamento (*Budget*) antes de começar e rode `terraform destroy` ao terminar os testes para não ter surpresas na fatura.

### Projeto 3: Plataforma completa em um cluster local

**Módulos:** Orquestração, Observabilidade, Plataforma.

1. Suba um cluster com o [Minikube]({{ '/content/guides/ferramentas-locais/#minikube' | relative_url }}) e instale o ArgoCD.
2. Crie um *Helm chart* para a aplicação do Projeto 1 e faça o deploy dela pelo ArgoCD (GitOps).
3. Instale a stack de observabilidade (Prometheus, Grafana, Loki e Jaeger) também pelo ArgoCD, e crie um *dashboard* no Grafana com as métricas da sua aplicação.
4. Configure um alerta no Prometheus (ex: aplicação fora do ar) e veja-o disparar.
5. Registre a aplicação no catálogo do Backstage, com links para o *dashboard* do Grafana e para a aplicação no ArgoCD.

**Diferencial:** use o padrão *App of Apps* do ArgoCD para que um único `kubectl apply` recrie todo o ambiente do zero.

### Como apresentar os seus projetos

Um projeto só conta no portfólio se outra pessoa conseguir entendê-lo. Capriche no `README.md` de cada repositório:

* **O que é e por que existe:** um parágrafo explicando o problema que o projeto resolve.
* **Diagrama da arquitetura:** uma imagem simples mostrando como as peças se conectam.
* **Como executar:** o passo a passo para qualquer pessoa rodar o projeto do zero.
* **Decisões e aprendizados:** por que você escolheu cada ferramenta e o que faria diferente.
* **Prints ou vídeo curto:** mostre o pipeline verde, o *dashboard* e o ArgoCD sincronizado.

Depois, compartilhe! Um post no LinkedIn contando o que você construiu e aprendeu ajuda outras pessoas e dá visibilidade ao seu trabalho.

{% include next-steps.html
   prev_url="/content/modules/proximos-passos/certificacoes/"
   prev_title="Certificações"
%}
