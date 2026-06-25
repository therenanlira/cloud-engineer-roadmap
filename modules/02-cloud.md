# Cloud Engineer Roadmap (DevOps/SRE/Platform)

## 2. Cloud

Cloud é o conceito de infraestrutura sob demanda, onde você contrata recursos de infraestrutura para executar suas aplicações, banco de dados, entre outros.
IaC (Infrastructure as Code; Infraestrutura como Código) é o conceito de criar esses recursos de infraestrutura em Cloud usando código, assim acelerando a replicação das configurações, padronizando e reduzindo erros humanos.

### 2.1. AWS (Amazon Web Services)

Seu primeiro contato com a nuvem pública. Use a camada gratuita (*Free Tier*) sempre que possível e lembre-se de limpar os recursos para evitar custos.

**Trilha de Estudo:**

* **Treinamento Oficial AWS (Gamificado):** [AWS Cloud Quest: Cloud Practitioner](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11458/aws-cloud-quest-cloud-practitioner) - Com missões práticas onde você usa um console AWS real em um ambiente de laboratório gratuíto, sem precisar usar o seu cartão de crédito.

* **Foco em Certificação (Opcional, pago):** [[Stephane Maarek] Ultimate AWS Certified Cloud Practitioner CLF-C02 2026](https://www.udemy.com/course/aws-certified-cloud-practitioner-new/?couponCode=PMNVD2025) - Se você tiver interesse em tirar uma certificação AWS, o curso do Stephane Maarek é uma excelente sugestão. Esse curso é pago e não é necessário para você seguir o roadmap.

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Cloud*
  * Faça os treinamentos:
    * AWS S3: Armazenamento de Objetos na Nuvem
    * AWS Lambda: Computação Serverless
    * AWS DynamoDB: Banco de Dados NoSQL

### 2.2. Terraform

Terraform é uma ferramenta de IaC open-source para provisionamento de infraesturura.

**Trilha de Estudo:**

* **Terraform para iniciantes:** [[LinuxTips] Terraform Essentials](https://linuxtips.io/treinamento/terraform-essentials/)

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Terraform*
  * Faça os treinamentos:
    * Terraform: Fundamentos de Infraestrutura como Código
    * Terraform: Provisioners e Módulos

### 2.3. FinOps (bônus)

Saber provisionar infraestrutura é o básico esperado; saber **quanto ela custa** e como otimizá-la é o que vai te destacar.

* **Alertas (Budgets):** O primeiro passo em qualquer conta cloud é criar um alerta de faturamento para evitar surpresas no cartão.
* **Visibilidade:** Crie o hábito de verificar o *AWS Cost Explorer* para entender como cada serviço (EC2, S3, RDS) impacta a fatura.
* **Arquitetura:** Entenda como os diferentes tipos de arquitetura de processadores (x64, ARM) podem impactar os custos. Entenda como cada serviços do Cloud Provider funciona para escolher o melhor recurso para a sua aplicação (EC2 vs Lambda, por exemplo).
* **Ferramentas da Comunidade:** Procure projetos abertos focados em gestão de custos da AWS, como o [InfraCost](https://github.com/infracost/infracost) e o [Amazon EC2 Instances Comparison](https://instances.vantage.sh).

---

### Checkpoint: Desafio Prático (Cloud)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para o reforçar o conhecimento.

**Objetivo**: Juntar os seus conhecimentos de AWS e Terraform e aplicá-los num ambiente controlado (local), sem custos.

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Cloud*
  * Faça os treinamentos:
    * Terraform com AWS: Construindo Infraestrutura em Nuvem
    * Desafio: AWS com Terraform

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.
