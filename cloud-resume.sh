#!/usr/bin/env bash
# cloud-resume.sh — 项目续温（只读）
# 用法: bash cloud-resume.sh OrgOps
set -euo pipefail

usage() {
  echo "用法: bash cloud-resume.sh <ProjectId>" >&2
  echo "示例: bash cloud-resume.sh OrgOps" >&2
  echo "只读：打印续温块、git 短状态、最新闸门文件。不改文件、不改主机环境。" >&2
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

PROJECT="${1:-}"
if [[ -z "$PROJECT" ]]; then
  usage
  exit 2
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJ_DIR="$ROOT/projects/$PROJECT"
BOARD="$PROJ_DIR/records/main/BOARD.md"
BACKLOG="$PROJ_DIR/records/main/BACKLOG.md"
PROJECT_MD="$PROJ_DIR/PROJECT.md"
RULES_MD="$PROJ_DIR/RULES.md"

fail=0
missing=()
for f in "$PROJECT_MD" "$RULES_MD" "$BOARD" "$BACKLOG"; do
  if [[ ! -f "$f" ]]; then
    missing+=("$f")
    fail=1
  fi
done

latest() {
  local dir="$1" glob="$2"
  local found=""
  if [[ -d "$dir" ]]; then
    found="$(find "$dir" -maxdepth 1 -type f -name "$glob" ! -name 'README.md' | sort | tail -n 1 || true)"
  fi
  if [[ -n "$found" ]]; then
    echo "$found"
  else
    echo "无"
  fi
}

one_line() {
  local path="$1"
  if [[ ! -f "$path" ]]; then
    echo "无"
    return
  fi
  local rel="${path#"$ROOT"/}"
  local hint
  hint="$(grep -E '^\| 闸门 \||^\| 焦点 \||^- \*\*结论' "$path" 2>/dev/null | head -n 1 | tr -d '\r' || true)"
  if [[ -z "$hint" ]]; then
    echo "$rel"
  else
    echo "$rel · ${hint}"
  fi
}

echo "## 续温"
echo "- Project：$PROJECT"
if [[ "$fail" -eq 1 ]]; then
  echo "- BOARD：缺文件（见下）"
  echo "- 最新 ARCH / EXEC / REVIEW / PM：无法读盘"
  echo "- 闸门状态：高断档"
  echo "- 断档风险：高（项目包不完整）"
  echo
  echo "缺文件："
  printf '  %s\n' "${missing[@]}"
  echo
  echo "已验证事实：本命令在 $ROOT 下以只读方式执行；未改主机环境。"
  exit 3
fi

echo "- BOARD：${BOARD#"$ROOT"/}"
echo "- BACKLOG：${BACKLOG#"$ROOT"/}"

arch="$(latest "$PROJ_DIR/records/lead-eng" "ARCH-*.md")"
exec_r="$(latest "$PROJ_DIR/records/exec" "EXEC-*.md")"
review="$(latest "$PROJ_DIR/records/review" "REVIEW-*.md")"
pm="$(latest "$PROJ_DIR/records/pm" "PM-*.md")"

echo "- 最新 ARCH：$(one_line "$arch")"
echo "- 最新 EXEC：$(one_line "$exec_r")"
echo "- 最新 REVIEW：$(one_line "$review")"
echo "- 最新 PM：$(one_line "$pm")"

gate="$(grep -E '^\| 闸门 \|' "$BOARD" | head -n 1 | sed 's/^| 闸门 |//;s/|$//;s/^[[:space:]]*//;s/[[:space:]]*$//' || true)"
focus="$(grep -E '^\| 焦点 \|' "$BOARD" | head -n 1 | sed 's/^| 焦点 |//;s/|$//;s/^[[:space:]]*//;s/[[:space:]]*$//' || true)"
echo "- 闸门状态：${gate:-未在 BOARD 找到闸门行}"
echo "- 焦点：${focus:-无}"
echo "- 断档风险：低（PROJECT / RULES / BOARD / BACKLOG 均在）"

echo
echo "## Git（短状态，不含 remote URL）"
if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "- 分支：$(git -C "$ROOT" branch --show-current 2>/dev/null || echo '?')"
  echo "- HEAD：$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo '?')"
  git -C "$ROOT" status -sb
else
  echo "- 非 git 工作区"
fi

if command -v gh >/dev/null 2>&1; then
  echo
  echo "## PR（当前分支，失败则忽略）"
  gh pr view --json url,title,isDraft,state -q '"- \(.state) draft=\(.isDraft) \(.title)\n- \(.url)"' 2>/dev/null || echo "- gh 不可用或当前分支无 PR"
fi

echo
echo "已验证事实：只读续温完成；未写入文件；未改主机环境。"
exit 0
