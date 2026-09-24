---
layout: default
title: Cloud (AWS)
---

# 2. Cloud

Cloud é o conceito de infraestrutura sob demanda, onde você contrata recursos de infraestrutura para executar suas aplicações, banco de dados, entre outros.
IaC (Infrastructure as Code; Infraestrutura como Código) é o conceito de criar esses recursos de infraestrutura em Cloud usando código, assim acelerando a replicação das configurações, padronizando e reduzindo erros humanos.

## AWS (Amazon Web Services)

Seu primeiro contato com a nuvem pública. Use a camada gratuita (*Free Tier*) sempre que possível e lembre-se de limpar os recursos para evitar custos.

**Trilha de Estudo:**

* <i class="fas fa-graduation-cap"></i> **Treinamento Oficial AWS:** [AWS Cloud Quest: Cloud Practitioner](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11458/aws-cloud-quest-cloud-practitioner) - Gamificado, com missões práticas que usa um console AWS real de laboratório gratuito, sem precisar criar conta.

> **Pensando em certificação?** Veja as sugestões de provas e cursos na página de [Certificações]({{ '/content/modules/proximos-passos/certificacoes/' | relative_url }}), no fim do roadmap.

**Laboratório Girus:** acesse o seu ambiente [Girus]({{ '/content/modules/introducao/preparacao-ambiente/' | relative_url }}), vá em Laboratórios e filtre por *Cloud*. Faça os seguintes treinamentos:

* AWS S3: Armazenamento de Objetos na Nuvem
* AWS Lambda: Computação Serverless
* AWS DynamoDB: Banco de Dados NoSQL

Pratique cada um desses laboratórios antes de seguir para o próximo tópico.

{% include next-steps.html
   prev_url="/content/modules/cloud/"
   prev_title="Cloud"
   next_url="/content/modules/cloud/terraform/"
   next_title="Terraform"
%}
