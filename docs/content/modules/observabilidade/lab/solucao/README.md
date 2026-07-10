# Solução do Desafio: Observabilidade (Módulo 5)

Este diretório contém a solução do desafio prático de Observabilidade. O objetivo deste projeto é instalar e configurar a stack padrão de mercado (Prometheus, Grafana, Loki e Jaeger) utilizando o Helm, proporcionando visibilidade completa sobre o que acontece dentro do seu cluster Kubernetes.

## 🗂️ Arquivos do Projeto

- **`hotrod.yaml`**: O manifesto que cria uma aplicação de demonstração oficial do Jaeger (chamada Hot R.O.D.). Ela já vem instrumentada com OpenTelemetry para gerar *traces* simulando chamadas a múltiplos microsserviços de um aplicativo de corridas.

*(Nota: Crie este arquivo no seu diretório para fazermos o deploy da aplicação de teste no final).*

## 🚀 Passo a Passo no Terminal

Abra o seu terminal e certifique-se de estar na pasta onde você criou o arquivo `hotrod.yaml`.

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

### 3. Instale a Stack de Observabilidade

Vamos instalar todas as ferramentas em um namespace separado chamado observability.

```bash
# Cria o namespace
kubectl create namespace observability

# Instala o Prometheus (Metrics)
helm install prometheus prometheus-community/prometheus --namespace observability

# Instala o Loki e o Promtail (Logs)
helm install loki grafana/loki-stack --namespace observability \

# Instala o Jaeger versão all-in-one em memória (Tracing)
helm install jaeger jaegertracing/jaeger --namespace observability --set provisionDataStore.cassandra=false --set allInOne.enabled=true --set storage.type=memory

# Instala o Grafana (Dashboards)
helm install grafana grafana/grafana --namespace observability \
-f grafana-values.yaml
```

### 4. Faça o deploy da aplicação de teste

Aplique o manifesto do Hot R.O.D. para termos dados reais passando pelas nossas ferramentas.

```bash
kubectl apply -f hotrod.yaml -n observability
```

### Acesse e Verifique o Resultado

As ferramentas estão rodando dentro do cluster. Para acessá-las pelo seu navegador, precisamos abrir as portas.

#### 1. Acessando e verificando o Grafana (Métricas e Logs)

Abra uma aba no seu terminal e execute:

```bash
# Redireciona a porta 3000
kubectl port-forward svc/grafana -n observability 3000:80
```

Descubra a senha:

```bash
kubectl get secret grafana -n observability -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

- Acesse [http://localhost:3000](http://localhost:3000) no navegador.
- Usuário: `admin`
- Senha: (a que você acabou de recuperar).

Visualize os dados:

- Para as Métricas: Vá em **Dashboards** e acesse o **Kubernetes resources usage monitoring (via Prometheus)**
- Para os Logs: Vá no menu **Explore**, selecione o **Loki** no topo, clique em **Label Filters** (ex: `app=hotrod` se estiver rodando a demo) e clique em **Run query** para ver os logs em tempo real.
- Para os Tracing: Vá no menu **Explore**, selecione o **Jaeger** no topo, na seleção de **Query type** clique em **Search**, em **Service name** escolha **jaeger** e clique em **Run query** para ver a lista de Tracing.

O Prometheus tem uma interface web que pode ser acessada sem a necessidade do Grafana. Abra outra aba no terminal e execute:

```bash
# Redirecione a porta do Prometheus
kubectl port-forward svc/prometheus-server -n observability 9090:80
```

#### 2. Acessando e verificando o Jaeger (Tracing)

Gerando traces manualmente:

```bash
kubectl run curl-test --rm -i --tty --image=curlimages/curl -n observability -- curl -s "http://hotrod:8080/dispatch?customer=123&nonse=1"
```

Abra outra aba no terminal e execute:

```bash
kubectl port-forward svc/jaeger -n observability 16686:16686
```

1. Acesse [http://localhost:16686](http://localhost:16686).
1. Na barra lateral esquerda (Search), selecione o serviço frontend (que é o nosso Hot R.O.D.) e clique em Find Traces.
1. Clique em um dos traces gerados para ver a "árvore" de requisições, identificando exatamente quantos milissegundos o banco de dados ou a API demoraram para responder.

### Limpando o ambiente

Ferramentas de observabilidade consomem bastante memória, pois estão constantemente coletando dados. Após finalizar os seus estudos, delete o cluster local:

```bash
minikube delete
# ou
kind delete cluster
```

### Resumo do Aprendizado

Neste desafio, você instalou os três pilares da Observabilidade Cloud Native. Agora você sabe como usar o Helm para provisionar infraestrutura complexa rapidamente e aprendeu a correlacionar os Gráficos de consumo (Prometheus/Grafana) com os Logs da aplicação (Loki) e o fluxo de requisições (Jaeger).
