# Cloud Infrastructure Engineer Roadmap

## TL;DR

Uma trilha de estudo de Engenheiro de Infraestrutura em Nuvem com conteúdos em Português. Termos e nomenclaturas poderão aparecer em Inglês, o que não é um impedimento para quem não domina o idioma.

Os materiais estão em vários formatos, como vídeos, artigos, documentação, livros e podcast. Todos os materiais são gratuitos, mas alguns complementos podem ser pagos.
Como o intuito é trazer materiais de estudo livres em Português, alguns cobrem apenas os fundamentos.

*Todos os créditos dos materiais aos autores que contribuem para a comunidade com o compartilhamento de conhecimento!*

## Roadmap (trilha)

A trilha é organizada por tópicos, como [Administração de Sistemas](https://github.com/therenanlira/cloud-engineer-roadmap#administra%C3%A7%C3%A3o-de-sistemas) e [Servidores](https://github.com/therenanlira/cloud-engineer-roadmap#servidores)). Os subtópicos são tecnologias ou ferramentas, como `Orquestração de contêineres` é um subtópico de [Infraestrutura em Nuvem](https://github.com/therenanlira/cloud-engineer-roadmap#infraestrutura-em-nuvem) e `Provisionamento de Infraestrutura` é um subtópico de [Infraestrutura como Código](https://github.com/therenanlira/cloud-engineer-roadmap#infraestrutura-como-c%C3%B3digo).

Clique na imagem para ampliar:

---

![alt text](https://raw.githubusercontent.com/therenanlira/roadmap-sre-devops/main/cloud-eng-roadmap.png)

---

## Introdução

### Ambiente

A maioria dos ambientes de estudos usam distribuições Linux/Unix.
Use o Sistema Operacional que preferir e o adapte para tirar melhor proveito dos treinamentos.
No Windows é possivel usar o WSL e no MacOS é possível alterar o Shell padrão para o Bash.

- [Aprenda a usar o WSL (Diolinux)](https://www.youtube.com/watch?v=o1_E4PBl30s)
- [Altere o Shell padrão no Terminal do Mac](https://support.apple.com/pt-br/guide/terminal/trml113/mac)

Se Linux é uma novidade, o treinamento da FIAP [Linux Fundamentals](https://eucapacito.com.br/curso-ec/linux-fundamentos/) pode ajudar.

## Materiais de estudo

Antes de começar, sugiro um estudo rápido sobre a cultura DevOps e a cultura Agile, e também sobre a Cloud Native Computing Foundation (CNCF).

<details><summary>Cultura DevOps</summary><p>

> A cultura DevOps é uma abordagem colaborativa e cultural que busca unir as equipes de desenvolvimento de software (Dev) e operações de TI (Ops) em um processo integrado e contínuo, visando acelerar a entrega de software, melhorar a qualidade dos produtos e aumentar a eficiência operacional.
> O termo "DevOps" combina as palavras "desenvolvimento" e "operações" para destacar a importância da colaboração entre essas duas áreas.
> Práticas e princípios-chave da cultura DevOps incluem a automação de processos, o uso de ferramentas de integração contínua e entrega contínua (CI/CD), a adoção de monitoramento e feedback contínuos, a implementação de testes automatizados e a busca por melhorias contínuas em todo o processo de desenvolvimento e implantação.

- Treinamento: [[FIAP] DevOps & Agile Culture](https://eucapacito.com.br/curso-ec/devops-agile-culture)

*OBS: os capítulos 1 e 2 apresentam a cultura DevOps, os capítulos seguintes apresentam a cultura Agile, que pode ser pulado caso queira focar apenas no tópico DevOps.*

</details>

<details><summary>Cloud Native Computing Foundation (CNCF)</summary><p>

> A Cloud Native Computing Foundation (CNCF) é uma organização sem fins lucrativos que tem como objetivo impulsionar a adoção e o desenvolvimento de tecnologias nativas da nuvem. Fundada em 2015 pela Linux Foundation, a CNCF fornece uma plataforma neutra para colaboração, padronização e promoção de soluções de código aberto voltadas para ambientes de nuvem.
> A CNCF é conhecida principalmente por seu projeto de orquestração de contêineres chamado Kubernetes, que se tornou um padrão de fato na indústria para gerenciar aplicativos em escala na nuvem. Além disso, a CNCF abriga uma variedade de outros projetos de código aberto relacionados, incluindo o Prometheus para monitoramento, o Envoy para proxy de serviços e o Fluentd para coleta e análise de logs, entre muitos outros.

- Oficial: [Cloud Native Computing Foundation](https://www.cncf.io/)
- Vídeo: [[IBM] O que é o Cloud Native](https://youtu.be/fp9_ubiKqFU)

</details>

### Administração de Sistemas

<details><summary>Monitoramento de processos</summary><p>

Um resumo do que é monitoramento de processos feito pelo ChatGPT:

> O monitoramento de processos é essencial para entender o desempenho do sistema, identificar gargalos, solucionar problemas e otimizar o uso de recursos. Ele desempenha um papel importante na administração de servidores, ambientes de produção e infraestrutura de TI em geral.

As principais ferramentas para monitoramento são `ps`, `top`, `htop`, e `kill`.

- Vídeo: [[LINUXtips] Gerenciamento de Processos Linux - ps, top, htop, kill](https://youtube.com/playlist?list=PLf-O3X2-mxDlx6sRx2WB-xv3Q9YHJ23ZN)

</details>

<details><summary>Manipulação de texto</summary><p>

Um resumo do que é a manipulação de texto feito pelo ChatGPT:

> A manipulação de texto em Linux refere-se à capacidade de processar e transformar dados de texto usando uma variedade de comandos e utilitários disponíveis no sistema operacional Linux. Essas ferramentas permitem realizar tarefas como busca, filtragem, substituição, formatação e processamento de arquivos de texto de maneira eficiente e automatizada.

Para um maior entendimento em como elas funcionam, use o comando [`man`](https://www.linuxforce.com.br/comandos-linux/comandos-linux-comando-man/) ou o comando [`tldr`](https://github.com/tldr-pages/tldr).

- `awk` - Uma linguagem de programação projetada para processamento de texto e normalmente usada como uma ferramenta de extração e relatórios de dados.
- `sed` - Um editor de fluxo para filtrar e transformar texto.
- `grep` - Um utilitário de linha de comando para pesquisar conjuntos de dados de texto simples para linhas que correspondem a uma expressão regular.
- `sort` - Um utilitário de linha de comando para classificar linhas de arquivos de texto.
- `cut` - Um utilitário de linha de comando para cortar seções de cada linha de arquivos.
- `uniq` - Um utilitário de linha de comando para relatar ou omitir linhas repetidas.
- `cat` - Um utilitário de linha de comando para concatenar arquivos e imprimir na saída padrão.
- `echo` - Um utilitário de linha de comando para exibir uma linha de texto.
- `fmt` - Um utilitário de linha de comando para formatação de texto ideal e simples.
- `tr` - Um utilitário de linha de comando para traduzir ou excluir caracteres.
- `nl` - Um utilitário de linha de comando para numerar linhas de arquivos.
- `wc` - Um utilitário de linha de comando para imprimir contagens de novas linhas, palavras e bytes para arquivos.

</details>

<details><summary>Ferramentas de rede</summary><p>

Um resumo do que são as ferramentas de rede feito pelo ChatGPT:

> As ferramentas de rede são conjuntos de utilitários e comandos disponíveis para gerenciar e diagnosticar redes em sistemas operacionais baseados em Linux. Essas ferramentas permitem aos administradores e usuários monitorar, configurar, solucionar problemas e interagir com redes de computadores.

Para um maior entendimento em como elas funcionam, use o comando [`man`](https://www.linuxforce.com.br/comandos-linux/comandos-linux-comando-man/) ou o comando [`tldr`](https://github.com/tldr-pages/tldr).

- `traceroute` - Rastreia a rota feita por pacotes em uma rede IP.
- `ping` - Envia pacotes de solicitação de eco para um host para testar a conexão com a Internet.
- `mtr` - Combina a funcionalidade de traceroute e ping em uma única ferramenta de diagnóstico.
- `nmap` - Verifica hosts em busca de portas abertas.
- `netstat` - Exibe conexões de rede, tabelas de roteamento, estatísticas de interface, conexões de mascarada e associações multicast.
- `ufw` e `firewalld` - Ferramenta de gerenciamento de Firewall.
- `iptables` e `nftables` - Ferramenta de gerenciamento de Firewall.
- `tcpdump` - Despeja o tráfego em uma rede.
- `dig` - Utilitário de pesquisa de DNS.
- `scp` - Cópia segura.

</details>

<details>
<summary>Desenvolvimento de scripts</summary>
<p>

- Um resumo do que é bash scripting feito pelo ChatGPT:

> Bash scripting é a prática de escrever scripts ou programas utilizando a linguagem de script Bash, que é uma shell de linha de comando amplamente usada em sistemas operacionais baseados em Unix, como Linux. O Bash scripting permite automatizar tarefas repetitivas, executar sequências de comandos, criar scripts complexos e personalizar a interação com o sistema operacional.

Desenvolver scripts bash requer um editor de texto. Pode ser usada a IDE [`VS Code`](https://code.visualstudio.com/) ou um editor de texto para o Shell, como o [`VIM`](https://www.vim.org/) ou [`NANO`](https://www.nano-editor.org/)

- Vídeo: [[debxp] Curso Básico de Bash](https://youtube.com/playlist?list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7)
- Vídeo: [[LINUXtips] Agendar um Job de Primeira no Crontab](https://youtu.be/jVM8Y97dLik)

</details>

### Servidores

<details><summary>Protocolos</summary><p>

Um resumo do que são os protocolos feito pelo ChatGPT:

> Os protocolos de rede são conjuntos de regras e formatos padronizados que governam a comunicação entre dispositivos em uma rede de computadores. Cada protocolo define como os dados devem ser transmitidos, organizados e interpretados entre os dispositivos.

- FTP (File Transfer Protocol): É um protocolo usado para transferir arquivos entre sistemas em uma rede. Permite o upload e download de arquivos de um computador remoto para um computador local ou vice-versa.

- HTTP (Hypertext Transfer Protocol): É o protocolo usado para transferir dados entre um cliente (geralmente um navegador) e um servidor na World Wide Web. É amplamente utilizado para acessar sites, enviar solicitações e receber respostas, como carregar páginas da web.

- HTTPS (Hypertext Transfer Protocol Secure): É uma extensão do HTTP que utiliza criptografia SSL/TLS para fornecer uma conexão segura e criptografada entre um cliente e um servidor. É usado em sites que requerem segurança, como transações financeiras e autenticação.

- SSL (Secure Sockets Layer): É um protocolo de segurança legado usado para estabelecer uma conexão criptografada entre um cliente e um servidor. Foi amplamente substituído pelo TLS.

- TLS (Transport Layer Security): É o sucessor do SSL e é usado para fornecer segurança em comunicações pela Internet. Ele criptografa os dados transmitidos entre os dispositivos para proteger a confidencialidade e integridade das informações.

- DNS (Domain Name System): É um protocolo usado para traduzir nomes de domínio em endereços IP. Ele permite que os usuários acessem sites digitando um nome de domínio, em vez de ter que memorizar o endereço IP numérico correspondente.

- SSH (Secure Shell): É um protocolo que permite a conexão segura a dispositivos remotos em uma rede. Ele fornece autenticação e criptografia para proteger as comunicações, sendo amplamente utilizado para acesso remoto a servidores e transferência segura de arquivos.

</details>

<details><summary>Servidor Web</summary><p>

Um resumo do que é o Servidor Web Nginx feito pelo ChatGPT:

> Nginx é um servidor web de alto desempenho, conhecido por sua escalabilidade e eficiência. Ele é usado para hospedar sites estáticos ou dinâmicos, além de servir como proxy reverso para balanceamento de carga, cache e manipulação de solicitações HTTP. O Nginx também pode ser usado como servidor de arquivos estáticos ou como proxy para servidores de aplicativos.

- Oficial: [Nginx Documentation](https://nginx.org/en/docs/)
- Vídeo: [[CoffOps] Forma fácil e correta de instalar o Nginx no Ubuntu 20.04](https://youtube.com/watch?v=hn17w828I-w)

</details>

<details><summary>Banco de Dados</summary><p>

Um resumo do que é Banco de Dados Redis feito pelo ChatGPT:

> Redis é um banco de dados em memória de código aberto, que também pode ser visto como um servidor de armazenamento de chave-valor. Ele é projetado para fornecer alta velocidade e baixa latência, sendo amplamente utilizado como um cache distribuído, armazenamento de sessão, fila de mensagens e muito mais. O Redis também suporta estruturas de dados avançadas, como listas, conjuntos, hashes e sorted sets.

- Vídeo: [[Filipe Morelli Developer] Curso de Redis](https://youtube.com/playlist?list=PLWhiA_CuQkbA_nmwPvjxVUr4XucYUrYXi)

</details>

<details><summary>Transmissão</summary><p>

Um resumo do que é o Kafka feito pelo ChatGPT:

> Kafka é uma plataforma de streaming (transmissão) distribuída, projetada para lidar com o processamento em tempo real de fluxos de dados. Ele funciona como um sistema de mensagens de alto desempenho e armazena fluxos de eventos em tópicos. O Kafka é usado para casos de uso de streaming e enfileiramento, como ingestão de dados, processamento de eventos em tempo real, integração de sistemas e criação de pipelines de dados.

- Vídeo: [[Escola de Inteligência Artificial] Apache Kafka](https://youtube.com/playlist?list=PLzWDDw1w8cTRsUM3cLMxImrQRv8jrOTP0)  

</details>

### Infraestrutura em Nuvem

<details><summary>Cloud Providers</summary><p>

Um resumo do que é Cloud Providers feito pelo ChatGPT:

> Cloud Providers, ou provedores de nuvem, são empresas que oferecem serviços de computação em nuvem para indivíduos e organizações. Eles fornecem infraestrutura, recursos de computação, armazenamento, serviços de rede e uma variedade de outros serviços na forma de plataformas baseadas em nuvem.

Escolha um provedor de nuvem e foque os estudos neste. O importante nesse passo é aprender os fundamentos, a base.

- Treinamento: [[Microsoft] Azure AZ-900](https://learn.microsoft.com/pt-br/certifications/azure-fundamentals/)
- Treinamento: [[Amazon] AWS Cloud Practitioner](https://aws.amazon.com/pt/training/learn-about/cloud-practitioner/?la=sec&sec=role)
- Treinamento: [[Google] Cloud Engineer Learning Path](https://www.cloudskillsboost.google/journeys/11)

</details>

<details><summary>Orquestração de contêineres</summary><p>

Um resumo do que é o Docker e Kubernetes feito pelo ChatGPT:

> Docker é uma plataforma de código aberto que permite a criação, distribuição e execução de aplicativos em contêineres. Contêineres são ambientes isolados que empacotam um aplicativo e suas dependências, garantindo que ele funcione de maneira consistente em qualquer ambiente, desde o desenvolvimento até a produção.
> Kubernetes é uma plataforma de código aberto para orquestração e gerenciamento de contêineres. Ele fornece um ambiente robusto e escalável para implantar, dimensionar e gerenciar aplicativos em contêineres de maneira eficiente.
> Já a orquestração de contêineres é o processo de gerenciar, coordenar e automatizar a implantação, escalabilidade e operações de contêineres em um ambiente distribuído. Alguns exemplos populares de sistemas de orquestração de contêineres incluem o Kubernetes e Apache Mesos.

- Oficial: [docker.com](https://www.docker.com)
- Vídeo: [[LINUXtips] Descomplicando Docker](https://youtube.com/playlist?list=PLf-O3X2-mxDn1VpyU2q3fuI6YYeIWp5rR)

- Oficial: [kubernetes.io](https://kubernetes.io)
- Vídeo: [[Prof. Gustavo Leitão] Kubernetes](https://youtube.com/playlist?list=PLyScRVRVdr6X9ulCNbVAsaggKBabNjELi)
- Vídeo: [[LINUXtips] Multirão Kubernetes](https://youtube.com/playlist?list=PLf-O3X2-mxDli3suNEnRquFyKYdrFLm3t)

</details>

### Infraestrutura como Código

<details><summary>Provisionamento de Infraestrutura</summary><p>

Um resumo do que é Provisionamento de Infraestrutura feito pelo ChatGPT:

> O provisionamento de infraestrutura com Ansible é um processo de automação que permite configurar e provisionar recursos de infraestrutura, como servidores, redes e serviços, de forma rápida, consistente e repetível. O Ansible é uma ferramenta de automação de TI que permite definir e executar tarefas em hosts remotos usando um conjunto declarativo de instruções.

- Oficial: [ansible.com](https://www.ansible.com)
- Vídeo: [[LINUXtips] O Ansible gerenciando seus servidores](https://youtu.be/lqmuUuzA39Q)
- Artigo: [[Álvaro Bacelar] Simplificando o AWX](https://medium.com/@alvarobacelar/simplificando-o-awx-1-6-156237ed7a22)

</details>

<details><summary>Gerenciamento de configurações</summary><p>

Um resumo do que é Gerenciamento de Configurações feito pelo ChatGPT:

> O gerenciamento de configurações com Terraform é uma abordagem para provisionar e gerenciar recursos de infraestrutura usando o Terraform, uma ferramenta de infraestrutura como código (IaC). O Terraform permite definir e controlar de maneira declarativa a infraestrutura necessária para suportar um aplicativo ou serviço, independentemente do provedor de nuvem ou ambiente de implantação.

- Oficial [terraform.io](https://www.terraform.io)
- Vídeo: [[LINUXtips] Descomplicando o Terraform](https://www.youtube.com/live/4FellihAcV8)
- Vídeo: [[LINUXtips] Lucas de Souza - Terraform além do básico](https://www.youtube.com/live/P3aY4_vxzWQ)

</details>

<details><summary>Versionamento de código</summary><p>

- Um resumo do que é Versionamento de código e Git feito pelo ChatGPT:

> O versionamento de código é o processo de controlar e gerenciar as alterações feitas em um projeto de software ao longo do tempo. Ele envolve o uso de sistemas de controle de versão para registrar, acompanhar e organizar as diferentes versões do código-fonte.
> Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear alterações em projetos de desenvolvimento de software. Ele permite que várias pessoas trabalhem em um projeto simultaneamente, gerenciando diferentes versões dos arquivos e facilitando a colaboração entre os membros da equipe.

- Vídeo: [[Bonieky Lacerda] Curso Completo de GIT](https://youtu.be/OuOb1_qADBQ)
- Vídeo: [[LINUXtips] Descomplicando o ArgoCD e o GitOps!](https://youtu.be/TDvA2vAQCF8)
</details>

### Esteira contínua

<details><summary>Integração continua</summary><p>

Um resumo do que é Integração contínua com GitHub Actions feito pelo ChatGPT:

> A Integração Contínua (CI, do inglês Continuous Integration) é uma prática de desenvolvimento de software que envolve a integração frequente e automatizada de código fonte em um repositório compartilhado. Isso é feito por meio de uma esteira contínua (ou pipeline) que executa uma série de etapas automatizadas para verificar a qualidade do código e detectar problemas o mais cedo possível.
> O GitHub Actions é uma ferramenta de automação fornecida pelo GitHub que permite criar e personalizar pipelines de integração contínua diretamente em seu repositório. Com o GitHub Actions, você pode definir fluxos de trabalho (workflows) que serão acionados automaticamente em resposta a eventos específicos, como push de código, criação de pull requests ou programação regular.

- Vídeo: [[dogcode] Github Actions do Zero e na Prática](https://youtu.be/MIVx1qniNKY)

</details>

<details><summary>Entrega continua</summary><p>

Um resumo do que é Entrega continua com Spinnaker feito pelo ChatGPT:

> A Entrega Contínua (CD, do inglês Continuous Delivery) é uma abordagem de desenvolvimento de software que visa entregar as mudanças de código de forma confiável e automatizada para o ambiente de produção. Ela envolve a automação do processo de construção, teste e implantação, permitindo que as equipes entreguem alterações com mais rapidez e frequência.
> O Spinnaker é uma plataforma de orquestração de entrega contínua de código aberto que ajuda a automatizar o fluxo de trabalho de entrega de software. Ele oferece recursos avançados para implantar aplicativos em diferentes ambientes, como nuvens públicas, privadas e híbridas.

- Documentação: [[Spinnaker] Tutorial](https://spinnaker.io/docs/guides/tutorials/)
- Treinamento: [[Google] Como implementar implantações canário com Spinnaker e Istio](https://cloud.google.com/architecture/implementing-canary-deployments?hl=pt-br)

</details>

<details><summary>Repositório de imagens</summary><p>

Um resumo do que é um repositório de imagens feito pelo ChatGPT:

> Um repositório de imagens é um serviço ou plataforma que permite armazenar, organizar e distribuir imagens de contêineres. Essas imagens são usadas para criar e implantar contêineres em ambientes de nuvem, como Kubernetes ou Docker.

- Vídeo: [[Jonathan Baraldi] Aprenda a instalar o Harbor](https://youtu.be/8oxx2n4QQgM)

</details>

<details><summary>Repositório de artefatos</summary><p>

Um resumo do que é um repositório de artefatos feito pelo ChatGPT:

> Um repositório de artefatos é uma ferramenta ou plataforma que permite armazenar, gerenciar e distribuir artefatos de software. Esses artefatos podem incluir pacotes de código-fonte, bibliotecas, componentes, imagens de contêineres, scripts de implantação e outros artefatos relacionados ao desenvolvimento de software.
> O Nexus Repository Manager, comumente referido como Nexus, é um exemplo popular de repositório de artefatos. Ele é amplamente utilizado na comunidade de desenvolvimento de software para gerenciar e organizar artefatos em um ambiente centralizado. O Nexus oferece recursos poderosos para facilitar a colaboração, a rastreabilidade e a distribuição de artefatos.

- Vídeo: [[Codigo Natural] Repositório de artefatos: Aonde guardamos nossos softwares que criamos?](https://youtu.be/xlI0f9XNWzE)

</details>

### Automação

<details><summary>Linguagem de programação</summary><p>

- Um resumo do que é Python feito pelo ChatGPT:

> Uma linguagem de programação é uma forma de comunicação entre humanos e computadores. No contexto da infraestrutura em nuvem, as linguagens de programação desempenham um papel fundamental na automação, provisionamento e gerenciamento de recursos em plataformas de nuvem. Aqui estão algumas aplicações das linguagens de programação na área de infraestrutura em nuvem:

Escolha uma linguagem e foque os estudos nesta. O importante nesse passo é aprender a lógica de programação e os fundamentos, e entender como aplicar desenvolvimento de scripts e aplicações para automatizar tarefas em Infraestrutura.

- Treinamento: [[Diego Mariano] Introdução à linguagem Python](https://www.udemy.com/course/intro_python/)
- Podcast: [[Hipster Talks] Automação com Python](https://youtu.be/s_b79fuuIY4)
- Vídeo: [[Aprenda Go] Aprenda Go](https://youtube.com/playlist?list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg)

</details>

<details><summary>Gerenciamento de automações</summary><p>

- Um resumo do que é o Rundeck (um gerenciador de automações) feito pelo ChatGPT:

> Rundeck é uma plataforma de automação de operações e agendamento de tarefas desenvolvida para simplificar e gerenciar fluxos de trabalho complexos em ambientes de TI. Ela fornece uma interface amigável para automatizar e orquestrar tarefas em uma variedade de sistemas, como servidores, nuvens, bancos de dados, aplicativos e muito mais.

- Vídeo: [[LINUXtips] Infra Ágil - Rundeck](https://youtu.be/kE3wxQSMaio)

</details>

### Observabilidade

<details><summary>Logs</summary><p>

Um resumo do que são Logs feito pelo ChatGPT:

> Logs são registros estruturados de eventos que ocorrem em um sistema. Eles fornecem uma visão detalhada de eventos, erros, exceções e outras informações relevantes sobre o funcionamento de um sistema. Os logs geralmente são textuais e contêm informações como data/hora, nível de log, mensagem descritiva e contexto. Eles são usados para solucionar problemas, investigar falhas, rastrear eventos e fornecer auditoria.

Uma das ferramentas mais utilizadas para Logs é o Elasticsearch. Este treinamento do Waldemar Neto abrange várias ferramentas, o que é um ótimo ponto de partida.

- Vídeo: [[Waldemar Neto] Kubernetes: Configurando cluster no Minikube do zero com Elasticsearch + Kibana + APM + Node js](https://youtu.be/CqLB-tBYB2Q)

</details>

<details><summary>Métricas</summary><p>

Um resumo do que é Métricas feito pelo ChatGPT:

> Métricas são medidas quantitativas do desempenho e do comportamento de um sistema. Elas são coletadas em intervalos regulares e fornecem informações numéricas sobre o uso de recursos, a taxa de transferência, o tempo de resposta e outros aspectos importantes de um sistema. As métricas são usadas para monitorar a saúde do sistema, identificar tendências, detectar anomalias e tomar decisões baseadas em dados.

O Prometheus é o mais utilizado quando se fala de métricas para Infraestrutura em contêineres, como Kubernetes.

- Vídeo: [[LINUXtips] Aprenda a monitorar seu cluster Kubernetes](https://youtu.be/BXjLHhMiTmU)

</details>

<details><summary>Tracing</summary><p>

Um resumo do que é Tracing feito pelo ChatGPT:

> O tracing envolve a captura e o registro de informações sobre o fluxo de uma solicitação ou transação ao longo de um sistema distribuído. Ele rastreia o caminho percorrido por uma solicitação à medida que atravessa diferentes componentes e serviços. O tracing permite identificar gargalos de desempenho, analisar latências, entender a sequência de eventos e otimizar o tempo de resposta de uma solicitação complexa.

Nesse subtópico, temos duas ferramentas, o Dynatrace e o Datadog.

O Dynatrace tem uma área de treinamento chamada Dynatrace University, que está apenas em inglês e requer um contrato corporativo. Para este, temos um treinamento da FNC Solutions e a página oficial documentação.

Já o Datadog tem uma área de treinamento livre, mas também apenas em inglês. Em português temos o vídeo do Douglas Mugnos que traz uma introdução sobre esta ferramenta.

- Documentação: [Welcome to Dynatrace Documentation](https://www.dynatrace.com/support/help)
- Treinamento: [Dynatrace University](https://www.dynatrace.com/dynatrace-university/)
- Vídeo: [[FNC Solutions] Dynatrace](https://youtube.com/playlist?list=PLP6PnrFnAWF5xvF4Cyz_0eSStFprk96Ez)
- Treinamento: [Datadog Learning Paths](https://learn.datadoghq.com/pages/learning-paths)
- Vídeo [[Douglas Mugnos] Saiba o que é e como usar o Datadog](https://youtu.be/4HVPWzhNE8k)

</details>

### Cloud Design Patterns

<details><summary>Alta disponibilidade</summary><p>

Um resumo do que é Cloud Design Patterns e a Alta Disponibilidade feito pelo ChatGPT:

> Cloud Design Patterns são padrões arquiteturais que foram projetados para ajudar a criar aplicativos e sistemas escaláveis, resilientes e seguros em ambientes de nuvem.
> Padrão de Disponibilidade Geográfica: Envolve a implantação de aplicativos em várias regiões geográficas para fornecer alta disponibilidade e tolerância a falhas.
> Padrão de Balanceamento de Carga: Distribui o tráfego de entrada entre vários recursos computacionais para melhorar a disponibilidade e a capacidade de resposta.
> Padrão de Escala Automática: Permite que os recursos do sistema sejam dimensionados automaticamente com base na demanda, garantindo a disponibilidade e o desempenho adequados.
> Padrão de Cluster de Servidores: Agrupa servidores em um cluster para fornecer alta disponibilidade e equilíbrio de carga

</details>

<details><summary>Resiliência</summary><p>

Um resumo do que é Cloud Design Patterns e a Resiliência feito pelo ChatGPT:

> Cloud Design Patterns são padrões arquiteturais que foram projetados para ajudar a criar aplicativos e sistemas escaláveis, resilientes e seguros em ambientes de nuvem.
> Padrão de Failover: Fornece uma estratégia para mudar automaticamente para um sistema de backup ou alternativo em caso de falha do sistema principal.
> Padrão de Replicação de Dados: Replica dados em várias localizações para garantir a disponibilidade contínua e a recuperação de falhas.
> Padrão de Monitoramento e Auto-recuperação: Monitora constantemente o estado do sistema e toma medidas automáticas para recuperar-se de falhas ou degradação de desempenho.
> Padrão de Particionamento de Dados: Divide grandes conjuntos de dados em partições menores para melhorar o desempenho e a tolerância a falhas.

</details>

<details><summary>Segurança</summary><p>

Um resumo do que é Cloud Design Patterns e a Resiliência feito pelo ChatGPT:

> Cloud Design Patterns são padrões arquiteturais que foram projetados para ajudar a criar aplicativos e sistemas escaláveis, resilientes e seguros em ambientes de nuvem.
> Padrão de Perímetro de Segurança: Estabelece uma camada de proteção em torno do sistema para filtrar e controlar o acesso de entrada e saída.
> Padrão de Autenticação e Autorização: Implementa mecanismos de autenticação e autorização para controlar o acesso aos recursos do sistema.
> Padrão de Comunicação Segura: Usa protocolos de comunicação seguros, como SSL/TLS, para proteger a transferência de dados entre os componentes do sistema.
> Padrão de Armazenamento Seguro: Aplica medidas de segurança para proteger os dados armazenados, como criptografia de dados em repouso.

</details>
