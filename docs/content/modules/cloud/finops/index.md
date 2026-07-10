---
layout: default
title: Cloud (FinOps)
---

# 2. Cloud

Cloud é o conceito de infraestrutura sob demanda, onde você contrata recursos de infraestrutura para executar suas aplicações, banco de dados, entre outros.
IaC (Infrastructure as Code; Infraestrutura como Código) é o conceito de criar esses recursos de infraestrutura em Cloud usando código, assim acelerando a replicação das configurações, padronizando e reduzindo erros humanos.

## FinOps (bônus)

Saber provisionar infraestrutura é o básico esperado; saber **quanto ela custa** e como otimizá-la é o que vai te destacar.

* **Alertas (Budgets):** O primeiro passo em qualquer conta cloud é criar um alerta de faturamento para evitar surpresas no cartão.
* **Visibilidade:** Crie o hábito de verificar o *AWS Cost Explorer* para entender como cada serviço (EC2, S3, RDS) impacta a fatura.
* **Arquitetura:** Entenda como os diferentes tipos de arquitetura de processadores (x64, ARM) podem impactar os custos. Entenda como cada serviços do Cloud Provider funciona para escolher o melhor recurso para a sua aplicação (EC2 vs Lambda, por exemplo).
* **Ferramentas da Comunidade:** Procure projetos abertos focados em gestão de custos da AWS, como o [InfraCost](https://github.com/infracost/infracost) e o [Amazon EC2 Instances Comparison](https://instances.vantage.sh).

{% include next-steps.html
   prev_url="/content/modules/cloud/terraform/"
   prev_title="Terraform"
   next_url="/content/modules/cloud/lab/"
   next_title="Desafio (Cloud)"
%}
