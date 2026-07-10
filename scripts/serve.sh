#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export BUNDLE_GEMFILE="$REPO_ROOT/docs/content/Gemfile"

cd "$REPO_ROOT"

bundle install
bundle exec jekyll serve --source docs "$@"
