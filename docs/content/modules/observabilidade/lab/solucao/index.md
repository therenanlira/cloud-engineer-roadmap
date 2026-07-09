---
layout: default
title: Observabilidade (Desafio - Solução)
---

# Cloud Engineer Roadmap (DevOps/SRE/Platform)

Um guia de estudos para iniciantes de Cloud Engineer (DevOps/SRE/Platform) **gratuitos** e em **português**, com **laboratórios** e **desafios** para você evoluir a cada etapa.

## 5. Observabilidade

Observabilidade é a capacidade de entender o estado do sistema (aplicações e infraestrutura), seja por **logs**, **métricas** ou **tracing**.

## Solução para o desafio prático (Observabilidade)

O objetivo deste desafio é instalar e configurar a stack padrão de mercado (Prometheus, Grafana, Loki e Jaeger) utilizando o Helm, proporcionando visibilidade completa sobre o que acontece dentro do seu cluster Kubernetes.

### 1. Inicie o cluster local

```bash
# Escolha a sua ferramenta:
minikube start
# ou
kind create cluster
# ou
k3d cluster create "my-cluster-name"
```

### 2. Adicione os repositórios do Helm

O Helm precisa saber de onde baixar os pacotes de instalação dessas ferramentas.

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
helm repo update
```

### 3. Configure os Data Sources do Grafana

Crie o arquivo `grafana-values.yaml`. Ele já vem com o Prometheus, o Loki e o Jaeger pré-configurados como fontes de dados, além de um dashboard padrão de métricas do Kubernetes.

```yaml
{% include_relative grafana-values.yaml %}
```

### 4. Instale a stack de observabilidade

Vamos instalar todas as ferramentas em um namespace separado chamado `observability`.

```bash
# Cria o namespace
kubectl create namespace observability

# Instala o Prometheus (Metrics)
helm install prometheus prometheus-community/prometheus --namespace observability

# Instala o Loki e o Promtail (Logs)
helm install loki grafana/loki-stack --namespace observability

# Instala o Jaeger versão all-in-one em memória (Tracing)
helm install jaeger jaegertracing/jaeger --namespace observability --set provisionDataStore.cassandra=false --set allInOne.enabled=true --set storage.type=memory

# Instala o Grafana (Dashboards), usando o arquivo criado no passo anterior
helm install grafana grafana/grafana --namespace observability -f grafana-values.yaml
```

### 5. Faça o deploy da aplicação de teste

Crie o arquivo `hotrod.yaml`. Ele cria uma aplicação de demonstração oficial do Jaeger (chamada Hot R.O.D.), já instrumentada com OpenTelemetry para gerar *traces* simulando chamadas a múltiplos microsserviços de um aplicativo de corridas.

```yaml
{% include_relative hotrod.yaml %}
```

Aplique o manifesto para termos dados reais passando pelas nossas ferramentas.

```bash
kubectl apply -f hotrod.yaml -n observability
```

### 6. Acesse e verifique o resultado

As ferramentas estão rodando dentro do cluster. Para acessá-las pelo seu navegador, precisamos abrir as portas.

#### Grafana (métricas e logs)

Abra uma aba no seu terminal e execute:

```bash
# Redireciona a porta 3000
kubectl port-forward svc/grafana -n observability 3000:80
```

Descubra a senha:

```bash
kubectl get secret grafana -n observability -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

* Acesse [http://localhost:3000](http://localhost:3000) no navegador.
* Usuário: `admin`
* Senha: a que você acabou de recuperar.

Visualize os dados:

* **Métricas:** vá em **Dashboards** e acesse o **Kubernetes resources usage monitoring (via Prometheus)**.
* **Logs:** vá no menu **Explore**, selecione o **Loki** no topo, clique em **Label Filters** (ex: `app=hotrod`) e clique em **Run query** para ver os logs em tempo real.
* **Tracing:** vá no menu **Explore**, selecione o **Jaeger** no topo, em **Query type** clique em **Search**, em **Service name** escolha **jaeger** e clique em **Run query** para ver a lista de traces.

O Prometheus também tem uma interface web própria, sem precisar do Grafana. Abra outra aba no terminal e execute:

```bash
kubectl port-forward svc/prometheus-server -n observability 9090:80
```

#### Jaeger (tracing)

Gere alguns traces manualmente:

```bash
kubectl run curl-test --rm -i --tty --image=curlimages/curl -n observability -- curl -s "http://hotrod:8080/dispatch?customer=123&nonse=1"
```

Abra outra aba no terminal e execute:

```bash
kubectl port-forward svc/jaeger -n observability 16686:16686
```

1. Acesse [http://localhost:16686](http://localhost:16686).
2. Na barra lateral esquerda (**Search**), selecione o serviço `frontend` (que é o nosso Hot R.O.D.) e clique em **Find Traces**.
3. Clique em um dos traces gerados para ver a "árvore" de requisições, identificando exatamente quantos milissegundos o banco de dados ou a API demoraram para responder.

## Limpando o ambiente

Ferramentas de observabilidade consomem bastante memória, pois estão constantemente coletando dados. Após finalizar os seus estudos, delete o cluster local:

```bash
minikube delete
# ou
kind delete cluster
```

## Resumo do Aprendizado

Neste desafio, você instalou a "Santíssima Trindade" da Observabilidade Cloud Native. Agora você sabe como usar o Helm para provisionar infraestrutura complexa rapidamente e aprendeu a correlacionar os gráficos de consumo (Prometheus/Grafana) com os logs da aplicação (Loki) e o fluxo de requisições (Jaeger).

{% include next-steps.html
   prev_url="/content/modules/observabilidade/lab/"
   prev_title="Desafio (Observabilidade)"
   next_url="/content/modules/plataforma/"
   next_title="Plataforma"
%}
