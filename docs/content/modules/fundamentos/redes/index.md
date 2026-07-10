---
layout: default
title: Fundamentos (Redes)
---

# 1. Fundamentos

A base técnica indispensável: sistemas operacionais, redes, automação e contêineres.

## Redes

Redes é a disciplina que trata de como os computadores se comunicam, base para o funcionamento de qualquer sistema web.

**Trilha de Estudo:**

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

> **Dica:** Use os comandos [`man`](content/guides/man-tldr.md/#-1-o-comando-man-manual-oficial) ou [`tldr`](content/guides/man-tldr.md/#-2-o-comando-tldr-exemplos-práticos-e-rápidos) para conhecer as flags e ver exemplos de uso de cada ferramenta.

{% include next-steps.html
   prev_url="/content/modules/fundamentos/linux/"
   prev_title="Linux"
   next_url="/content/modules/fundamentos/scripts/"
   next_title="Scripts"
%}
