#!/usr/bin/env bash
set -euo pipefail
pytest -q --tb=short
TARGET_DIR="${1:-.}"
TARGET_DIR="$(cd "$TARGET_DIR" 2>/dev/null && pwd -P || echo "$TARGET_DIR")"
find "$TARGET_DIR" -type f -printf "%s %p\n" 2>/dev/null |   sort -nrk1,1 |   head -n