# Criando uma imagem do Backstage

Para os próximos desafios, vamos precisar fazer alterações no Backstage que exigem alterar a imagem de container. Para isso vamos *buildar* a nossa própria imagem.

## 1. Inicie o projeto

Crie um diretório (ex.: `meu-backstage`) para o Backstage e execute o comando:

```bash
npx @backstage/create-app@latest
```

Esse comando irá gerar toda a estrutura necessária para o *build* da nossa imagem do Backstage.

### 2. Instale o projeto

Execute o comando para instalar os pacotes necessários:

```bash
yarn install
```
