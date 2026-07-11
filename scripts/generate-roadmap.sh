#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

python3 -m venv venv
source venv/bin/activate

if ! python3 -m pip show Pillow >> /dev/null 2>&1; then
  pip install Pillow
fi

python3 generate-roadmap.py

deactivate
