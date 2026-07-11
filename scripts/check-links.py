"""Checa links internos (href/src) e âncoras (#) de um site já buildado.

Uso: python3 scripts/check-links.py <diretorio-do-site> [baseurl]
O baseurl (ex: /cloud-engineer-roadmap) deve ser informado quando o site foi
buildado com esse prefixo, para os links absolutos resolverem corretamente.
Sai com código 1 se encontrar qualquer link ou âncora quebrada.
"""

import os
import re
import sys
import urllib.parse

LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
ID_RE = re.compile(r'id="([^"]+)"')

BASEURL = ""


def resolve(site, page_dir, url):
    path = urllib.parse.unquote(url)
    if BASEURL and (path == BASEURL or path.startswith(BASEURL + "/")):
        path = path[len(BASEURL):] or "/"
    if path.startswith("/"):
        fs = os.path.join(site, path.lstrip("/"))
    else:
        fs = os.path.normpath(os.path.join(page_dir, path))
    if fs.endswith("/"):
        fs = os.path.join(fs, "index.html")
    elif os.path.isdir(fs):
        fs = os.path.join(fs, "index.html")
    return fs


def main(site):
    broken = []
    ids_cache = {}

    def ids_of(path):
        if path not in ids_cache:
            with open(path, encoding="utf-8") as f:
                ids_cache[path] = set(ID_RE.findall(f.read()))
        return ids_cache[path]

    for root, _dirs, files in os.walk(site):
        for fn in files:
            if not fn.endswith(".html"):
                continue
            page = os.path.join(root, fn)
            with open(page, encoding="utf-8") as f:
                html = f.read()
            page_ids = None
            for match in LINK_RE.finditer(html):
                url = match.group(1)
                if url.startswith(("http://", "https://", "mailto:", "data:")):
                    continue
                base, _, frag = url.partition("#")
                base = base.split("?")[0]
                frag = urllib.parse.unquote(frag)

                if base:
                    target = resolve(site, root, base)
                    if not os.path.exists(target):
                        broken.append((page, url, "arquivo não existe"))
                        continue
                else:
                    target = page

                if frag and target.endswith(".html"):
                    if target == page:
                        if page_ids is None:
                            page_ids = set(ID_RE.findall(html))
                        found = frag in page_ids
                    else:
                        found = frag in ids_of(target)
                    if not found:
                        broken.append((page, url, "âncora não existe"))

    for page, url, reason in broken:
        print(f"{os.path.relpath(page, site)}: {url} ({reason})")
    print(f"{len(broken)} link(s) quebrado(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print(__doc__)
        sys.exit(2)
    if len(sys.argv) == 3:
        BASEURL = sys.argv[2].rstrip("/")
    sys.exit(main(sys.argv[1]))
