---
layout: default
title: Observabilidade (Desafio)
---

# Cloud Engineer Roadmap (DevOps/SRE/Platform)

Um guia de estudos para iniciantes de Cloud Engineer (DevOps/SRE/Platform) **gratuitos** e em **português**, com **laboratórios** e **desafios** para você evoluir a cada etapa.

## 5. Observabilidade

Observabilidade é a capacidade de entender o estado do sistema (aplicações e infraestrutura), seja por **logs**, **métricas** ou **tracing**.

### Desafio Prático (Observabilidade)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para o reforçar o conhecimento.

**Objetivo:** Obter visibilidade completa do seu cluster local implementando os três pilares da observabilidade (Metrics, Logs e Tracing) num ambiente controlado (local) e sem custos.

**Passo a passo do desafio:**

1. **Setup:** Suba o seu cluster local e garanta que o [Helm](https://helm.sh/pt/docs/intro/install) esteja instalado no seu ambiente local.
2. **Infraestrutura:** Utilize o Helm para provisionar a "Santíssima Trindade" da Observabilidade:
   * **Métricas:** Prometheus.
   * **Logs:** Loki (com Promtail).
   * **Tracing:** Jaeger (versão `all-in-one`).
   * **Visualização:** Grafana.
3. **Integração:** Configure os *Data Sources* no Grafana para conectar as três fontes de dados em um único painel centralizado.
4. **Instrumentação e Tracing:** Faça o deploy da aplicação de demonstração [Hot R.O.D.](https://github.com/jaegertracing/jaeger/tree/main/examples/hotrod) e utilize comandos efêmeros (`kubectl run`) ou acesse a interface web da aplicação para gerar tráfego de rede e observar os *traces* sendo capturados em tempo real.

**Solução:** A solução para este desafio está [aqui](./solucao/), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.

{% include next-steps.html
   prev_url="/content/modules/observabilidade/jaeger/"
   prev_title="Jaeger"
   next_url="/content/modules/plataforma/"
   next_title="Plataforma"
%}
