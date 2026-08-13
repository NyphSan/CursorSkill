#!/usr/bin/env bash
# orgops-loop.sh — 跑一轮 OrgOps 长期环（升格 + 度量 + CYCLE 报告）
# 用法: bash scripts/orgops-loop.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
export CURSOR_MODEL="${CURSOR_MODEL:-cursor-grok-4.6-high}"

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git fetch origin CursorSkillSearch:refs/remotes/origin/CursorSkillSearch 2>/dev/null || true
fi

python3 "$ROOT/scripts/orgops_cycle.py" \
  --root "$ROOT" \
  --digest-ref origin/CursorSkillSearch \
  --started-at "$STARTED" \
  --model "$CURSOR_MODEL" \
  --session-id "${CURSOR_SESSION_ID:-}"
