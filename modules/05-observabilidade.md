# Cloud Engineer Roadmap (DevOps/SRE/Platform)

## 5. Observabilidade

Observabilidade é a capacidade de entender o estado do sistema (aplicações e infraestrutura), seja por **logs**, **métricas** ou **tracing**.

### 5.1. Grafana (Gráficos)

Grafana é a ferramenta open-source de visualização de gráficos mais popular.

* **Introdução ao Grafana:** [[Estudando DevOps] Introdução ao Grafana | Ferramenta de Observabilidade | Monitoramento](https://youtu.be/RDIax5pDmCc)

### 5.2. Prometheus (Metrics)

Métricas são dados quantitativos (CPU, memória, taxa de erro) que mostram a saúde do seu sistema.
Prometheus é a ferramenta open-source mais usada em Kubernetes.

**Trilha de Estudo:**

* **Aprofundamento em Metrics e AlertManager:** [[Fabricio Veronez] Prometheus + AlertManager no Kubernetes: Monitoramento além do dashboard](https://youtu.be/NTRLWcryaCA)
* **Consultas avançadas no Prometheus::** [[Fabricio Veronez] Guia Prático de PromQL: Aprenda do Zero a Consultar Métricas no Prometheus](https://youtu.be/U8_lQBbQQow)

### 5.3. Logs (Loki)

Logs são registros de eventos que ocorrem em tempo real.
Loki é uma ferramenta open-source de gerenciamento de logs da mesma empresa do Grafana, a GrafanaLabs.

**Trilha de Estudo:**

* **Vídeo introdução com práticas de Grafana Loki:** [[Fabricio Veronez] Logs na Prática: Implementação com Grafana Loki](https://youtu.be/aDKixwnEz-A)

### 5.4. Jaeger (Tracing)

Tracing é uma técnica para rastrear o fluxo das requisições através de múltiplos microsserviços. Essencial em sistemas distribuídos.
Jaeger é uma plataforma open-source de tracing.

**Trilha de Estudo:**

* **Vídeo introdutório:**[[Fabricio Veronez] OpenTelemetry do Zero: Guia Rápido para Devs, SREs e DevOps](https://youtu.be/8JfIeoFoHl0)
* **Maior aprofundamento:** [[Fabricio Veronez] Tracing com OpenTelemetry e Jaeger](https://youtube.com/playlist?list=PLP6PnrFnAWF5xvF4Cyz_0eSStFprk96Ez)

---

### Checkpoint: Desafio Prático (Observabilidade)

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

**Solução:** A solução para este desafio está [aqui](desafios/module-05/README.md), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.
