# Scripts

Ferramentas de apoio ao projeto. Nenhum arquivo aqui faz parte do site publicado
(o site em si vive em [`docs/`](../docs)); são scripts de desenvolvimento local.

## `serve.sh`

Sobe o site Jekyll localmente para testar mudanças antes de publicar.

```bash
./scripts/serve.sh
```

O site tem o próprio `Gemfile`, que fica em `docs/`. Você pode executar os comandos `bundle` diretamente ou utilizar o script `serve.sh`, que executa o seguinte:

1. Aponta o Bundler para `docs/Gemfile` (via `BUNDLE_GEMFILE`), não
   importa de qual diretório você o execute.
2. Roda `bundle install`.
3. Roda `bundle exec jekyll serve --source docs`, apontando o Jekyll para a
   pasta correta.

Qualquer argumento extra é repassado direto para o `jekyll serve`, por exemplo:

```bash
./scripts/serve.sh --port 4001 --livereload
```

Acesse `http://127.0.0.1:4000` (ou a porta escolhida) para ver o site.

**Requisitos:** Ruby + [Bundler](https://bundler.io/) instalados.

## `generate-roadmap.py` / `generate-roadmap.sh`

Gera a imagem `docs/assets/img/cloud-eng-roadmap.png` (o diagrama do roadmap
usado no `README.md`) a partir da lista de módulos definida no próprio
`generate-roadmap.py`.

```bash
./scripts/generate-roadmap.sh
```

O script `.sh` cria uma virtualenv Python temporária em `scripts/venv`, instala o [Pillow](https://python-pillow.org/) se
necessário e executa o `generate-roadmap.py`. O `.py` procura uma fonte
Arial/Liberation/DejaVu típica de macOS, Linux ou Windows e cai para a fonte
padrão do Pillow se nenhuma for encontrada; não precisa ajustar nada por SO.

Rode este script sempre que a lista de módulos do roadmap mudar (novo módulo,
título ou reordenação) para manter a imagem em `README.md` e na home do site
sincronizada com o conteúdo real.

**Requisitos:** Python 3.

## `check-links.py`

Checa todos os links internos e âncoras de um site já buildado. É o mesmo
script que o CI (`.github/workflows/ci.yml`) executa antes de fazer o deploy
do site no GitHub Pages.

```bash
bundle exec jekyll build --source docs --destination _site
python3 scripts/check-links.py _site
```

Se o site foi buildado com `--baseurl`, informe o mesmo prefixo como segundo
argumento (ex: `python3 scripts/check-links.py _site /cloud-engineer-roadmap`).

**Requisitos:** Python 3 (sem dependências externas).
