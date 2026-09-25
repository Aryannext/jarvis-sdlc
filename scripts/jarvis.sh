#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JARVIS_HOME="$(cd "$SCRIPT_DIR/.." && pwd)"

if ! command -v claude >/dev/null 2>&1; then
  echo "Error: Claude Code no está instalado o no está en PATH." >&2
  exit 1
fi

exec claude --add-dir "$JARVIS_HOME" "$@"
