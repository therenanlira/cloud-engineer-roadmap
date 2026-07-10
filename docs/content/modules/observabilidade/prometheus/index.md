---
layout: default
title: Observabilidade (Prometheus)
---

# 5. Observabilidade

Observabilidade é a capacidade de entender o estado do sistema (aplicações e infraestrutura), seja por **logs**, **métricas** ou **tracing**.

## Prometheus (Metrics)

Métricas são dados quantitativos (CPU, memória, taxa de erro) que mostram a saúde do seu sistema.
Prometheus é a ferramenta open-source mais usada em Kubernetes.

**Trilha de Estudo:**

* <i class="fas fa-video"></i> **Aprofundamento em Metrics e AlertManager:** [[Fabricio Veronez] Prometheus + AlertManager no Kubernetes: Monitoramento além do dashboard](https://youtu.be/NTRLWcryaCA)
* <i class="fas fa-video"></i> **Consultas avançadas no Prometheus:** [[Fabricio Veronez] Guia Prático de PromQL: Aprenda do Zero a Consultar Métricas no Prometheus](https://youtu.be/U8_lQBbQQow)

Depois de dominar as métricas, siga para os logs com o Loki.

{% include next-steps.html
   prev_url="/content/modules/observabilidade/grafana/"
   prev_title="Grafana"
   next_url="/content/modules/observabilidade/loki/"
   next_title="Loki"
%}
