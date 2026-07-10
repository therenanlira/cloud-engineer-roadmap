---
layout: default
title: Observabilidade (Loki)
---

# 5. Observabilidade

Observabilidade é a capacidade de entender o estado do sistema (aplicações e infraestrutura), seja por **logs**, **métricas** ou **tracing**.

## Loki (Logs)

Logs são registros de eventos que ocorrem em tempo real.
Loki é uma ferramenta open-source de gerenciamento de logs da mesma empresa do Grafana, a GrafanaLabs.

**Trilha de Estudo:**

* **Vídeo introdução com práticas de Grafana Loki:** [[Fabricio Veronez] Logs na Prática: Implementação com Grafana Loki](https://youtu.be/aDKixwnEz-A)

Com métricas e logs cobertos, falta apenas o tracing para fechar os três pilares da observabilidade.

{% include next-steps.html
   prev_url="/content/modules/observabilidade/prometheus/"
   prev_title="Prometheus"
   next_url="/content/modules/observabilidade/jaeger/"
   next_title="Jaeger"
%}
