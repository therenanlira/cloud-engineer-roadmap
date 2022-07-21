
# **Roadmap SRE DevOps**

## **O que é?**

Essa é mais uma das muitas trilhas de estudo para SRE / DevOps que tem pela Internet à fora, mas o objetivo desta é apresentar desde a base às ferramentas mais utilizadas em grandes ambientes, junto com dicas de materiais para estudo, a maioria em português.

## **Como funciona?**

O Roadmap é separado em três fases. Cada fase agrupa tópicos próximos tecnicamente, o que ajuda o aprendizado a fluir melhor.

Está disponível vários materiais em vídeos, artigos, documentação, livros e podcast. A maioria são materiais gratuitos que possuem conteúdo básico e intermediário mas, alguns, também traz conteúdo avançado. 

*Todos os créditos do materiais aos autores que contribuem para a comunidade com o compartilhamento de conhecimento!*

Por serem materiais gratuitos, pode conter venda de cursos e outros. Se sentir a vontade e gostar do conteúdo, não hesite em comprar e ajudar a galera.

## **Ok, cadê o Roadmap?**

Está aqui (clique na imagem para ampliar):

![alt text](https://raw.githubusercontent.com/therenanlira/roadmap-sre-devops/main/roadmap-sre-devops.png)
  

## **E os materiais de estudo?**

Antes, é bom informar que a maioria dos materiais de estudos usam como base distribuições Linux.  
No Sistema Operacional Windows pode ser utilizado o WSL2 e no MacOS pode ser alterar o shell de zsh para bash:

-   [Aprenda a usar o WSL (Diolinux)](https://www.youtube.com/watch?v=o1_E4PBl30s):
-   (Opcional) [Altere o Shell padrão no Terminal do Mac](https://support.apple.com/pt-br/guide/terminal/trml113/mac)


### **Fase 1**
Objetivo: Na Fase 1 vamos estudar a base da infraestrutura, administração de serviços e desenvolvimento. O objetivo é entender o funcionamento da camada abaixo dos microsserviços, que será estudada na Fase 2.

1. **System Administration**

    - **Linux Server:**
        - [Curso - Linux Fundamentals (4Linux)](http://confluence.viavarejo.com.br/-%20https:/4linux.com.br/cursos/treinamento/linux-fundamentals/)
		- [Curso - Linux Essentials (4Linux)](https://4linux.com.br/cursos/treinamento/linux-essentials/)
		- [Vídeo - Curso de terminal linux (Daniel Berg)](https://youtu.be/VRR3V42EdSg)
		- [Vídeo - Curso básico de programação em Bash (debxp)](https://youtu.be/ZM--I3NJ2jY)
		- [Vídeo - Gerenciamento de Processos de Linux (LINUXtips)](https://youtu.be/-bEVlQv_O-8)
		- [Vídeo - Tudo sobre permissões avançadas e ACL no Linux (LINUXtips)](https://youtu.be/tT69ipXOzfc)
		- [Vídeo - Administrando volumes com LVM (LINUXtips)](https://youtu.be/Oxv2tHcraV8)
		- [Vídeo - O que é o SYSTEMD? E como usá-lo! (LINUXtips)](https://youtu.be/1uGqXhhberk)
		- [Vídeo - Como usar o Editor VIM #1 (LINUXtips)](https://youtu.be/XXRZ0acXHU0)
		- [Vídeo - Como usar o Editor VIM #2 (LINUXtips)](https://youtu.be/_qShvkx8jK0)
		- [Vídeo - Como usar o Editor VIM #3 (LINUXtips)](https://youtu.be/_hJkHTmedEk)
		- [Vídeo - Descomplicando o Gerenciamento de Logs no Linux (LINUXtips)](https://youtu.be/ujdEF-f2iEs)
		- [Vídeo - Criando um Servidor de Logs remoto no Linux (LINUXtips)](https://youtu.be/iK4l-gDCCBs)
		- [Vídeo - Dominando os Logs no Linux com JournalCTL (LINUXtips)](https://youtu.be/jT9yjpUYB-Y)
		- [Vídeo - Como aumentar a sua performance no Linux? (LINUXtips)](https://youtu.be/X0fRA_MSkx4)
		- [Artigo - Configurar SSL Seguro](https://tested-resistance-7fc.notion.site/SSH-secure-d254d355fa34465aa683e186bb31e845)  
    
    - **Windows Server:**
		- [Vídeo - Windows Server 2019 (ProfessorRamos)](https://youtube.com/playlist?list=PL35Zp8zig6smTjTNrP3bPUu6DHitjrxq_)
		- [Vídeo - PowerShell (ProfessorRamos)](https://youtube.com/playlist?list=PL35Zp8zig6slB_EaLbwKP57L9weBfICtS)  

---
2. **Network**

    - **OSI Model**
		- [Vídeo - Fundamentos de Redes de Computadores (Glauko Carvalho)](https://youtu.be/vqrvOz1zSgY)

    - **TCP/IP Protocol**
	    -  [Vídeo - Protocolos de Redes de Computadores (Glauko Carvalho)](https://youtu.be/kP1kktlbUTs)  
    
---
3. **Servers**

    - **Web server**
		- [Vídeo - NGINX (O Servidor Web pensado em Performance e Escala) (Código Fonte TV)](https://youtu.be/YXLI5Rbu_Ek)
        - [Vídeo - NGINX, um poderoso serviço HTTP/HTTPS e Proxy reverso (aiedonline)](https://youtu.be/JAFFkDKvZlo)
		- [Doc - Nginx Documentation (Oficial)](https://nginx.org/en/docs/)
		- [Vídeo - Instalando Servidor WEB IIS (ProfessorRamos)](https://youtu.be/SD4TXosi9LI)
		- [Vídeo - Servidor WEB IIS - Configurando Registro DNS (ProfessorRamos)](https://youtu.be/M8Hb5x72BPI)
		- [Vídeo - Servidor WEB IIS - Hospedando dois Sites (ProfessorRamos)](https://youtu.be/AhneVTu8yf4)  
    
	- **Automation**
		- [Vídeo - Agendar um Job de Primeira no Crontab (LINUXtips)](https://youtu.be/jVM8Y97dLik)
		- [Vídeo - Rundeck (LINUXtips)](https://youtu.be/kE3wxQSMaio)  
    
	- **Monitoring**
		- [Vídeo - Treinamento base Zabbix 6.0 (Magno Monte Cerqueira)](https://youtube.com/playlist?list=PLCFBm2AvdHoBn7lbiP6d8ef1l74hAjXvo)

	- **Caching**
		- [Vídeo - Curso de Redis (Filipe Morelli Developer)](https://youtube.com/playlist?list=PLWhiA_CuQkbA_nmwPvjxVUr4XucYUrYXi)
		- [Opcional: Vídeo - Learn to use Redis with Python and Flask (yingshaoxo's lab)](https://youtu.be/CC_7BlTUtGw)  
 
	 - **Streaming**
		- [Vídeo - Apache Kafka (Escola de Inteligência Artificial)](https://youtube.com/playlist?list=PLzWDDw1w8cTRsUM3cLMxImrQRv8jrOTP0)  

---
4.  **Database**

	- **SQL**
		- [Vídeo - SQL Sem mistério: Introdução (RafaBrito)](https://youtube.com/playlist?list=PL6D9EMPMNdExSDbnRfwNhdTq1C1UQryo3)

	- **PostgreSQL**
		- [Vídeo - Banco de Dados com PostgreSQL (Descompila)](https://youtube.com/playlist?list=PLWd_VnthxxLe660ABLFZH26CW3G-uQIv-)  

	- **SQL Server**
		- [Vídeo - Primeiros Passos no SQL Server (Hashtag Programação)](https://youtu.be/rwHv1DvyiCc)  

	- **NoSQL**
		- [Vídeo - Bancos de Dados: Relacionais x Não Relacionais (Larissa Falcão)](https://youtu.be/qVXIsdcHnmQ)  

	- **MongoDB**
		- [Vídeo - Curso de MongoDB para iniciantes (Nataniel Paiva Oficial)](https://youtube.com/playlist?list=PLxuFqIk29JL0DMM0Z-S9_XEHAexXvhYyb)

---
5.  **Version Control**

	- **Git**
		- [Vídeo - Descomplicando o GIT: Conheça a ferramenta criada por Linux Torvalds (LINUXtips)](https://youtu.be/_aj3hsEh9iw)  

	- **GitHub**
		- [Vídeo - Curso Completo de GIT (Bonieky Lacerda)](https://youtu.be/OuOb1_qADBQ)

---
6.  **Development**

	 - **Programming Logic**
		- [Curso - Lógica de Programação com JavaScript (4Linux)](https://4linux.com.br/cursos/treinamento/logica-programacao-gratuito/)  

	- **Python**
		- [Curso - Introdução à linguagem Python (Diego Mariano - Udemy)](https://www.udemy.com/course/intro_python/)
		- [Vídeo - Projeto completo com PYSCRIPT | TODO-LIST (pythonando)](https://youtu.be/_N0bxwb_CJo)
		- [Vídeo - Python - Curso Flask (Filipe Morelli Developer)](https://youtube.com/playlist?list=PLWhiA_CuQkbBhvPojHOPY81BmDt2eSfgI)
		- [Vídeo - Automação WEB Selenium com Python (Didática Tech)](https://youtube.com/playlist?list=PLyqOvdQmGdTS1NP14Bo7OADsfy9woYGIk)
		- [Vídeo - Automatize Tarefas Maçantes com Python (Geofisicando)](https://youtube.com/playlist?list=PLLCFxfe9wkl-5oz4YIOxMzbBGP1FaGm3T)
		- [Opcional: Vídeo - Flask MongoDB Todo App (Code With Prince)](https://youtube.com/playlist?list=PLU7aW4OZeUzwN0TsZLZUuzhc0f7OVVBcT)
		- [Opcional: Podcast - Automação com Python (Hipster.Talks)](https://youtu.be/s_b79fuuIY4)
		- [Livro - Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
		- [Artigo - Dockerizando micro serviços em Python (Rafael Cirolini)](https://cirolini.medium.com/dockerizando-microservi%C3%A7os-em-python-bcaedd6da3c4)  
    
	- **Golang**
		- [Vídeo - Aprenda Go (Aprenda Go)](https://youtube.com/playlist?list=PLCKpcjBB_VlBsxJ9IseNxFllf-UFEXOdg)


---
**Fase 2**

*Em desenvolvimento*


---
**Fase 3**

*Em desenvolvimento*
