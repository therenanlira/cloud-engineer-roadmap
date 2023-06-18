# **Cloud Infrastructure Engineer Roadmap**

## **TL;DR**

Uma trilha de estudo de Infraestrutura em Nuvem com a maior parte do conteúdo em Português. Porém, termos e nomenclaturas poderão ser apresentadas em Inglês, o que não é um impedimento para quem não domina o idioma.

Os materiais estão em vários formatos, como vídeos, artigos, documentação, livros e podcast. Todos os materiais são gratuitos, mas alguns complementos podem ser pagos.

*Todos os créditos dos materiais aos autores que contribuem para a comunidade com o compartilhamento de conhecimento!*

## **Roadmap**

A trilha é organizada por contexto, como [Fundamentos](https://example.com) e [Administração de Sistemas](https://example.com). Os tópicos são tecnologias ou ferramentas relacionadas ao contexto, como `Cloud Native Computing Foundations` é um tópico de [Fundamentos](https://example.com) e `Monitoramento de processos` é um tópico de [Administração de Sistemas].
Os contextos são independentes, caso queira pular direto para um contexto específico, veja os tópicos relacionados.

Clique na imagem para ampliar:

![alt text](https://raw.githubusercontent.com/therenanlira/roadmap-sre-devops/main/cloud-eng-roadmap.png)

## **Materiais**

A maioria dos ambientes de estudos usam distribuições Linux/Unix.
Use o Sistema Operacional que preferir e o adapte para tirar melhor proveito dos treinamentos.
No Windows é possivel usar o WSL e no MacOS é possível alterar o Shell padrão para o Bash, se preferir:

- [Aprenda a usar o WSL (Diolinux)](https://www.youtube.com/watch?v=o1_E4PBl30s):
- [Altere o Shell padrão no Terminal do Mac](https://support.apple.com/pt-br/guide/terminal/trml113/mac)

Se Linux é uma novidade, o treinamento da FIAP [Linux Fundamentals](https://eucapacito.com.br/curso-ec/linux-fundamentos/) pode ajudar.

### **Fundamentos**

<details>
<summary>Cloud Native Computing Foundation</summary>
<p>

- Um resumo do que é a CNCF feito pelo ChatGPT:

> A Cloud Native Computing Foundation (CNCF) é uma organização sem fins lucrativos que tem como objetivo impulsionar a adoção e o desenvolvimento de tecnologias nativas da nuvem. Fundada em 2015 pela Linux Foundation, a CNCF fornece uma plataforma neutra para colaboração, padronização e promoção de soluções de código aberto voltadas para ambientes de nuvem.
> A CNCF é conhecida principalmente por seu projeto de orquestração de contêineres chamado Kubernetes, que se tornou um padrão de fato na indústria para gerenciar aplicativos em escala na nuvem. Além disso, a CNCF abriga uma variedade de outros projetos de código aberto relacionados, incluindo o Prometheus para monitoramento, o Envoy para proxy de serviços e o Fluentd para coleta e análise de logs, entre muitos outros.

- Oficial: [Cloud Native Computing Foundation](https://www.cncf.io/)
- Vídeo: [[IBM] O que é o Cloud Native](https://youtu.be/fp9_ubiKqFU)

</p>
</details>

<details>
<summary>Cultura DevOps</summary>
<p>

- Um resumo do que é a CNCF feito pelo ChatGPT:

> A cultura DevOps é uma abordagem colaborativa e cultural que busca unir as equipes de desenvolvimento de software (Dev) e operações de TI (Ops) em um processo integrado e contínuo, visando acelerar a entrega de software, melhorar a qualidade dos produtos e aumentar a eficiência operacional.
> O termo "DevOps" combina as palavras "desenvolvimento" e "operações" para destacar a importância da colaboração entre essas duas áreas.
> Práticas e princípios-chave da cultura DevOps incluem a automação de processos, o uso de ferramentas de integração contínua e entrega contínua (CI/CD), a adoção de monitoramento e feedback contínuos, a implementação de testes automatizados e a busca por melhorias contínuas em todo o processo de desenvolvimento e implantação.

- Treinamento: [[FIAP] DevOps & Agile Culture](https://eucapacito.com.br/curso-ec/devops-agile-culture)
  - OBS: nos capítulos 1 e 2 é apresentado a cultura DevOps, nos capítulos 3 à 5 é apresentado a cultura Agile, que pode ser pulado, caso queira focar apenas no assunto DevOps.

</details>

### Administração de Sistemas

<details>
<summary>Monitoramento de processos</summary>
<p>

- Um resumo do que é monitoramento de processos feito pelo ChatGPT:

> O monitoramento de processos é essencial para entender o desempenho do sistema, identificar gargalos, solucionar problemas e otimizar o uso de recursos. Ele desempenha um papel importante na administração de servidores, ambientes de produção e infraestrutura de TI em geral.

As principais ferramentas para monitoramento são `ps`, `top`, `htop`, e `kill`.

- Vídeo: [[LinuxTips] Gerenciamento de Processos Linux - ps, top, htop, kill](https://youtube.com/playlist?list=PLf-O3X2-mxDlx6sRx2WB-xv3Q9YHJ23ZN)

</p>
</details>

<details>
<summary>Ferramentas de rede</summary>
<p>

- Um resumo do que são as ferramentas de rede feito pelo ChatGPT:

> As ferramentas de rede são conjuntos de utilitários e comandos disponíveis para gerenciar e diagnosticar redes em sistemas operacionais baseados em Linux. Essas ferramentas permitem aos administradores e usuários monitorar, configurar, solucionar problemas e interagir com redes de computadores.

Essas ferramentas mais utilizadas, para um maior entendimento em como elas funcionam, use o comando [`man`](https://www.linuxforce.com.br/comandos-linux/comandos-linux-comando-man/) ou o comando [`tldr`](https://github.com/tldr-pages/tldr).

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

</p>
</details>

<details>
<summary>Manipulação de texto</summary>
<p>

- Um resumo do que é a manipulação de texto feito pelo ChatGPT:

> A manipulação de texto em Linux refere-se à capacidade de processar e transformar dados de texto usando uma variedade de comandos e utilitários disponíveis no sistema operacional Linux. Essas ferramentas permitem realizar tarefas como busca, filtragem, substituição, formatação e processamento de arquivos de texto de maneira eficiente e automatizada.

Essas ferramentas mais utilizadas, para um maior entendimento em como elas funcionam, use o comando [`man`](https://www.linuxforce.com.br/comandos-linux/comandos-linux-comando-man/) ou o comando [`tldr`](https://github.com/tldr-pages/tldr).

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

</p>
</details>

<details>
<summary>Desenvolvimento de scripts</summary>
<p>

- Um resumo do que é bash scripting feito pelo ChatGPT:

> Bash scripting é a prática de escrever scripts ou programas utilizando a linguagem de script Bash, que é uma shell de linha de comando amplamente usada em sistemas operacionais baseados em Unix, como Linux. O Bash scripting permite automatizar tarefas repetitivas, executar sequências de comandos, criar scripts complexos e personalizar a interação com o sistema operacional.

Desenvolver scripts bash requer um editor de texto. Pode ser usada a IDE [`VS Code`](https://code.visualstudio.com/) ou um editor de texto para o Shell, como o [`VIM`](https://www.vim.org/) ou [`NANO`](https://www.nano-editor.org/)

- Vídeo: [[debxp] Curso Básico de Bash](https://youtube.com/playlist?list=PLXoSGejyuQGpf4X-NdGjvSlEFZhn2f2H7)
- Vídeo: [[LinuxTips] Agendar um Job de Primeira no Crontab](https://youtu.be/jVM8Y97dLik)

</p>
</details>

### Servidores

<details>
<summary>Protocólos</summary>
<p>

- Um resumo do que são os protocólos feito pelo ChatGPT:

> Os protocolos de rede são conjuntos de regras e formatos padronizados que governam a comunicação entre dispositivos em uma rede de computadores. Cada protocolo define como os dados devem ser transmitidos, organizados e interpretados entre os dispositivos.

- FTP (File Transfer Protocol): É um protocolo usado para transferir arquivos entre sistemas em uma rede. Permite o upload e download de arquivos de um computador remoto para um computador local ou vice-versa.

- HTTP (Hypertext Transfer Protocol): É o protocolo usado para transferir dados entre um cliente (geralmente um navegador) e um servidor na World Wide Web. É amplamente utilizado para acessar sites, enviar solicitações e receber respostas, como carregar páginas da web.

- HTTPS (Hypertext Transfer Protocol Secure): É uma extensão do HTTP que utiliza criptografia SSL/TLS para fornecer uma conexão segura e criptografada entre um cliente e um servidor. É usado em sites que requerem segurança, como transações financeiras e autenticação.

- SSL (Secure Sockets Layer): É um protocolo de segurança legado usado para estabelecer uma conexão criptografada entre um cliente e um servidor. Foi amplamente substituído pelo TLS.

- TLS (Transport Layer Security): É o sucessor do SSL e é usado para fornecer segurança em comunicações pela Internet. Ele criptografa os dados transmitidos entre os dispositivos para proteger a confidencialidade e integridade das informações.

- DNS (Domain Name System): É um protocolo usado para traduzir nomes de domínio em endereços IP. Ele permite que os usuários acessem sites digitando um nome de domínio, em vez de ter que memorizar o endereço IP numérico correspondente.

- SSH (Secure Shell): É um protocolo que permite a conexão segura a dispositivos remotos em uma rede. Ele fornece autenticação e criptografia para proteger as comunicações, sendo amplamente utilizado para acesso remoto a servidores e transferência segura de arquivos.

</p>
</details>

<details>
<summary>Servidores</summary>
<p>

- Um resumo do que são servidores feito pelo ChatGPT:

> Servidor, no contexto de tecnologia, refere-se a um software ou hardware que oferece serviços ou recursos para outros dispositivos ou aplicativos em uma rede. Esses servidores são projetados para atender a solicitações, processar dados e fornecer funcionalidades específicas.
> Cada um desses servidores desempenha um papel específico em diferentes cenários de aplicativos e infraestrutura de TI. O Nginx é amplamente utilizado como servidor web e proxy reverso, o Redis é conhecido por sua velocidade e flexibilidade como banco de dados em memória, e o Kafka é uma plataforma de streaming de alto desempenho para lidar com fluxos contínuos de dados em tempo real.

- Nginx é um servidor web de alto desempenho, conhecido por sua escalabilidade e eficiência. Ele é usado para hospedar sites estáticos ou dinâmicos, além de servir como proxy reverso para balanceamento de carga, cache e manipulação de solicitações HTTP. O Nginx também pode ser usado como servidor de arquivos estáticos ou como proxy para servidores de aplicativos.

- Redis é um banco de dados em memória de código aberto, que também pode ser visto como um servidor de armazenamento de chave-valor. Ele é projetado para fornecer alta velocidade e baixa latência, sendo amplamente utilizado como um cache distribuído, armazenamento de sessão, fila de mensagens e muito mais. O Redis também suporta estruturas de dados avançadas, como listas, conjuntos, hashes e sorted sets.

- Kafka é uma plataforma de streaming distribuída, projetada para lidar com o processamento em tempo real de fluxos de dados. Ele funciona como um sistema de mensagens de alto desempenho e armazena fluxos de eventos em tópicos. O Kafka é usado para casos de uso de streaming, como ingestão de dados, processamento de eventos em tempo real, integração de sistemas e criação de pipelines de dados.

- Oficial: [Nginx Documentation](https://nginx.org/en/docs/)
- Vídeo: [[CofOps] Forma fácil e correta de instalar o Nginx no Ubuntu 20.04](https://youtube.com/watch?v=hn17w828I-w)
- Vídeo: [[Filipe Morelli Developer] Curso de Redis](https://youtube.com/playlist?list=PLWhiA_CuQkbA_nmwPvjxVUr4XucYUrYXi)
- Vídeo: [[Escola de Inteligência Artificial] Apache Kafka](https://youtube.com/playlist?list=PLzWDDw1w8cTRsUM3cLMxImrQRv8jrOTP0)  

</p>
</details>

### Containers

<details>
<summary>Docker</summary>
<p>

</p>
</details>

<details>
<summary>Kubernetes</summary>
<p>

</p>
</details>

### Cloud Infrastructure

<details>
<summary>Azure</summary>
<p>

</p>
</details>

<details>
<summary>GCP</summary>
<p>

</p>
</details>

<details>
<summary>AWS</summary>
<p>

</p>
</details>

### Infraestrutura como Código

<details>
<summary>Git</summary>
<p>

- Um resumo do que é Git feito pelo ChatGPT:

> Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear alterações em projetos de desenvolvimento de software. Ele permite que várias pessoas trabalhem em um projeto simultaneamente, gerenciando diferentes versões dos arquivos e facilitando a colaboração entre os membros da equipe.

- Vídeo: [[Bonieky Lacerda] Curso Completo de GIT](https://youtu.be/OuOb1_qADBQ)

</p>
</details>

<details>
<summary>GitOps</summary>
<p>

</p>
</details>

<details>
<summary>Ansible</summary>
<p>

</p>
</details>

<details>
<summary>Terraform</summary>
<p>

</p>
</details>

### Esteira contínua

<details>
<summary>GitHub Actions</summary>
<p>

</p>
</details>

<details>
<summary>Spinnaker</summary>
<p>

</p>
</details>

<details>
<summary>Nexus</summary>
<p>

</p>
</details>

<details>
<summary>Harbor</summary>
<p>

</p>
</details>

### Automação

<details>
<summary>Python</summary>
<p>

- Um resumo do que é Python feito pelo ChatGPT:

> Python é uma linguagem de programação interpretada, de alto nível e de propósito geral. Foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Python é conhecida por sua simplicidade, clareza de código e facilidade de leitura, o que a torna uma ótima opção tanto para iniciantes quanto para desenvolvedores experientes.

- Treinamento: [[Diego Mariano] Introdução à linguagem Python](https://www.udemy.com/course/intro_python/)
- Livro: [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- Podcast: [[Hipster Talks] Automação com Python](https://youtu.be/s_b79fuuIY4)

</p>
</details>

<details>
<summary>Go</summary>
<p>

- Um resumo do que é Go feito pelo ChatGPT:

> Golang, também conhecida como Go, é uma linguagem de programação moderna, de código aberto, desenvolvida pelo Google. Ela foi projetada para ser eficiente, simples, segura e de fácil leitura. Go foi lançada em 2009 e ganhou popularidade devido à sua eficiência no desenvolvimento de sistemas escaláveis e concorrentes.

- Vídeo: [[Aprenda Go] Aprenda Go](https://youtube.com/playlist?list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg)

</p>
</details>

<details>
<summary>Rundeck</summary>
<p>

- Um resumo do que é Rundeck feito pelo ChatGPT:

> Rundeck é uma plataforma de automação de operações e agendamento de tarefas desenvolvida para simplificar e gerenciar fluxos de trabalho complexos em ambientes de TI. Ela fornece uma interface amigável para automatizar e orquestrar tarefas em uma variedade de sistemas, como servidores, nuvens, bancos de dados, aplicativos e muito mais.

- Vídeo: [[LinuxTips] Infra Ágil - Rundeck](https://youtu.be/kE3wxQSMaio)

</p>
</details>

### Observabilidade

<details>
<summary>Prometheus</summary>
<p>

</p>
</details>

<details>
<summary>Grafana</summary>
<p>

</p>
</details>

<details>
<summary>Elastic</summary>
<p>

</p>
</details>

<details>
<summary>Dynatrace</summary>
<p>

</p>
</details>

### Cloud Design Patterns

<details>
<summary>Alta disponibilidade</summary>
<p>

</p>
</details>

<details>
<summary>Resiliência</summary>
<p>

</p>
</details>

<details>
<summary>Segurança</summary>
<p>

</p>
</details>
