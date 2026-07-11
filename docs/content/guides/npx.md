---
layout: default
title: Guia (npx)
permalink: /content/guides/npx/
---

# Guia: Como instalar o `npx`

Várias ferramentas (como o `@backstage/create-app`) são distribuídas como pacotes do npm e executadas via `npx`, sem precisar instalar nada globalmente antes. Este guia mostra como deixar o `npx` disponível no seu terminal.

---

## 1. O que é o `npx`

O `npx` é um executor de pacotes que vem junto com o `npm` (desde a versão 5.2). Ele baixa (ou usa uma versão já instalada) e executa um pacote do npm sem exigir uma instalação global permanente, por exemplo:

```bash
npx @backstage/create-app@latest
```

Como o `npx` vem embutido no `npm`, e o `npm` vem embutido no Node.js, instalar o `npx` na prática significa **instalar o Node.js**.

## 2. Como instalar

### No macOS

Usando o [Homebrew](https://brew.sh):

```bash
brew install node
```

### No Linux (Ubuntu / Debian / WSL)

A versão empacotada pelo `apt` costuma ficar desatualizada. Prefira o [NodeSource](https://github.com/nodesource/distributions):

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

### No Windows

Baixe o instalador **LTS** direto do [site oficial do Node.js](https://nodejs.org) e siga o assistente.

### Alternativa multiplataforma (recomendada): nvm

O [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager) permite instalar e alternar entre várias versões do Node sem precisar de `sudo`, e funciona igual em macOS e Linux (no Windows, use o [nvm-windows](https://github.com/coreybutler/nvm-windows)):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash
nvm install --lts
```

## 3. Verifique a instalação

```bash
node --version
npm --version
npx --version
```

Se os três comandos retornarem um número de versão (e não um erro de "comando não encontrado"), está tudo pronto para usar o `npx`.
