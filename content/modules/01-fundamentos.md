# Cloud Engineer Roadmap (DevOps/SRE/Platform)

## 1. Fundamentos

A base técnica indispensável: sistemas operacionais, redes, automação e contêineres.

### 1.1. Linux & Redes

Linux é a base de tudo, é o Sistema Operacional mais utilizado em servidores, por conta disso, deve ser aprendido em primeiro lugar.

Redes é a disciplica que trata de como os computadores se comunicam, sendo a base para o funcionamento de sistemas web.

**Trilha de Estudo:**

* **Linux para iniciantes:** [[LinuxTips] Linux Essentials](https://linuxtips.io/treinamento/linux-essentials/)
* **Redes para iniciantes:** Entenda os conceitos dos protocólos de rede e as ferramentas. Guarde bem esse conhecimento, pois serão muito utilizados mais a frente nos laboratórios de Docker em diante.

#### Protocolos de Rede

Esses protocolos são essenciais para a administração de servidores, comunicação entre microsserviços e segurança na nuvem:

* `DNS (Domain Name System)`: É o protocolo usado para traduzir nomes de domínio (como google.com) em endereços IP. Ele permite que os recursos na nuvem se comuniquem por nomes em vez de IPs dinâmicos.
* `SSH (Secure Shell)`: É um protocolo que permite a conexão segura e criptografada a dispositivos e servidores remotos. Essencial para administrar instâncias Linux na nuvem via terminal.
* `TCP / UDP`: Protocolos da camada de transporte. O TCP garante a entrega ordenada e confiável dos dados (usado por HTTP, SSH), enquanto o UDP prioriza a velocidade (usado por DNS).
* `HTTP (Hypertext Transfer Protocol)`: É o protocolo usado para transferir dados na Web. É a base da comunicação de quase todas as APIs modernas e microsserviços.
* `HTTPS (Hypertext Transfer Protocol Secure)`: É uma extensão segura do HTTP que utiliza criptografia SSL/TLS para proteger os dados transmitidos entre o cliente e o servidor.
* `SSL (Secure Sockets Layer) / TLS (Transport Layer Security)`: Protocolos de segurança usados para criptografar conexões na internet. O TLS é o sucessor moderno e seguro do antigo SSL (hoje legado).

#### Ferramentas de Rede

Essas ferramentas são essenciais para testar conexões, mapear portas, configurar firewalls e analisar o tráfego da rede:

* `ping` - Envia pacotes ICMP para testar a conectividade básica com um host na internet.
* `traceroute` / `mtr` - Rastreia a rota feita por pacotes em uma rede IP até o destino, mostrando cada salto (hop). O mtr traz essa análise em tempo real.
* `nmap` - Verifica hosts ativos e faz escaneamento de portas abertas para fins de segurança e descoberta de serviços na rede.
* `ss` / `netstat` - Exibe conexões de rede ativas, tabelas de roteamento e estatísticas de interface diretamente no servidor.
* `dig` - Utilitário essencial para realizar consultas DNS e diagnosticar problemas de resolução de nomes.
* `tcpdump` - Captura e analisa pacotes de dados que trafegam na interface de rede em tempo real (packet sniffer).
* `ufw` / `firewalld` - Interfaces amigáveis para gerenciamento de Firewall no Linux (Ubuntu/Debian e CentOS/RHEL, respectivamente).
* `iptables` e `nftables` - Ferramenta de baixo nível para filtragem de pacotes e regras de firewall do próprio kernel Linux.

> **Dica:** Use os comandos [`man`](content/guidesman-tldr.md/#-1-o-comando-man-manual-oficial) ou [`tldr`](content/guidesman-tldr.md/#-2-o-comando-tldr-exemplos-práticos-e-rápidos) para conhecer as flags e ver exemplos de uso de cada ferramenta.

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Linux*
  * Faça os treinamentos:
    * Processamento de Texto no Linux: grep, sed, awk
    * Monitoramento Básico do Sistema Linux
    * Gerenciamento e Monitoramento de Processos no Linux
    * Administração de Usuários e Grupos no Linux
    * Permissões de Arquivos no Linux

### 1.3. Scripts & Git

Automação e controle de versão do seu código.

#### Scripts (Bash)

Bash é um dos interpretadores de comandos do Linux, com ele conseguimos criar arquivos com comandos (Shell Scripts) para automatizar tarefas repetitivas.

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Linux*
  * Faça os treinamentos:
    * Introdução ao Shell Script Bash

#### Scripts (Python)

Python é uma das linguagens de programação mais usada em infraestrutura para automações por conta da sua sintaxe simples.

**Trilha de Estudo:**

* **Curso introdutório:** [[Diego Mariano] Introdução à linguagem Python](https://www.udemy.com/course/intro_python/)
* **Maior aprofundamento:** [[LinuxTips] Python Essentials](https://linuxtips.io/treinamento/python-essentials/)

#### Git & GitHub

Git é um sistema de versionamento de código, muito útil para criar versões do seu código e "voltar no tempo" quando alguma alteração não funcionar como esperada.
GitHub é a plataforma de hospedagem de código mais popular, baseada em Git.

**Trilha de Estudo:**

* **GitHub para iniciantes:** [[LinuxTips] GitHub Essentials](https://linuxtips.io/treinamento/github-essentials/)

### 1.4. Containers (Docker)

Contêiner é uma forma de isolar um ambiente para executar códigos, aplicações e asim por diante.
Docker é a ferramenta de criação e execução de contêineres.

**Trilha de Estudo:**

* **Vídeo introdutório:** [[Mayk Brito] Como funciona o Docker? (explicação SIMPLES)](https://youtu.be/IY-ceuwqnns)
* **Docker para iniciantes:** [[LinuxTips] Docker Essentials](https://linuxtips.io/treinamento/docker-essentials/)

**Laboratórios:**

* Laboratório Girus:
  * Acesse o seu ambiente Girus
  * Vá em Laboratórios
  * Filtre por *Docker*
  * Faça os treinamentos:
    * Introdução ao Docker
    * Gerenciamento de Containers Docker
    * Redes no Docker: Conceitos e Implementação
    * Persistência de Dados com Docker Volumes
    * Introdução ao Docker Compose

---

### Checkpoint: Desafio Prático (Fundamentos)

Antes de avançar, aplique o que aprendeu. Este desafio é fundamental para o reforçar o conhecimento.

**Objetivo**: Juntar os seus conhecimentos de Linux, Redes, Scripts e Docker para criar uma página web simples que monitora a conectividade de outros sites.

**Cenário**: Você precisa subir um contêiner Nginx que sirva um arquivo de texto simples contendo o status de conectividade de alguns sites, gerado automaticamente por um script Bash.

**Passo a passo do desafio**:

* **Python:** Crie um script em Python (`monitor.py`) utilizando a biblioteca `requests` para testar os sites. O desafio aqui é entender como gerenciar dependências de bibliotecas externas dentro de um container Docker (usando `pip install`).
* **Processamento de texto:** O script deve salvar o resultado desses testes formatado dentro de um arquivo chamado `status.txt` (ex: `Google: Online`, `SiteFalso: Offline`). Lembre-se de dar as permissões de execução (`chmod +x`) ao seu script.
* **Docker:** Crie um `Dockerfile` utilizando a imagem oficial do `nginx`. O seu Dockerfile deve copiar o arquivo `status.txt` para a pasta padrão que o Nginx usa (`/usr/share/nginx/html`).
* **Redes:** Faça o build da sua imagem (`docker build -t monitor-site .`) e rode o contêiner mapeando a porta `8080` do seu computador para a porta `80` do contêiner (`docker run -p 8080:80 monitor-site`).
* **Validação:** Abra o seu navegador e acesse <http://localhost:8080/status.txt> (ou use o comando `curl localhost:8080/status.txt` no terminal) para ver o relatório de conectividade gerado pelo seu script.
* **Bash**: Crie um único script chamado `deploy.sh` que executa o `monitor.py`, faz o `docker build` e o `docker run` de forma sequencial.

**Solução:** A solução para este desafio está [aqui](content/labs/module-01/README.md), mas consulte somente se não conseguir resolver por si só.

> **Aviso de Recursos:** Este laboratório exige recursos locais (CPU/RAM). Certifique-se de encerrar o ambiente após os testes para liberar espaço.
