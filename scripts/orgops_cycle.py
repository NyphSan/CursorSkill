#!/usr/bin/env python3
"""OrgOps one cycle: promote DIGEST 引入 skills, write CYCLE report."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

MAX_PROMOTE = 3
MAP_BEGIN = "<!-- ORGOPS_SKILL_MAP_BEGIN -->"
MAP_END = "<!-- ORGOPS_SKILL_MAP_END -->"
DIGEST_REF_DEFAULT = "origin/CursorSkillSearch"


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def git_show(root: Path, spec: str) -> str | None:
    p = run(["git", "show", spec], cwd=root, check=False)
    if p.returncode != 0:
        return None
    return p.stdout


def parse_digest_introduces(digest: str) -> list[str]:
    names: list[str] = []
    for line in digest.splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 2:
            continue
        name, last = cols[0], cols[-1]
        if name in {"名称", ""} or set(name) <= {"-"}:
            continue
        if "不直接入库" in last or "观望" in last:
            continue
        if "引入" in last:
            names.append(name.strip("`"))
    return names


def find_skill_dir(root: Path, ref: str, name: str) -> str | None:
    p = run(["git", "ls-tree", "-r", "--name-only", ref], cwd=root, check=False)
    if p.returncode != 0:
        return None
    suffix = f"/{name}/SKILL.md"
    hits = [ln for ln in p.stdout.splitlines() if ln.endswith(suffix) and ln.startswith("skills/")]
    if len(hits) == 1:
        return str(Path(hits[0]).parent)
    if len(hits) > 1:
        return str(Path(hits[0]).parent)
    return None


def license_ok(source: str) -> bool:
    if re.search(r"(?i)无\s*LICENSE|no license|license:\s*none", source):
        if re.search(r"(?i)\*\*LICENSE\*\*\s*:\s*MIT", source):
            return True
        if "本轮收录前已就绪" in source or re.search(r"(?i)LICENSE.*MIT", source):
            return True
        return False
    return bool(re.search(r"(?i)LICENSE", source)) and bool(
        re.search(r"(?i)\b(MIT|Apache-2\.0|BSD|ISC|CC-BY)\b", source)
    )


def already_authoritative(skill_map: str, name: str) -> bool:
    for line in skill_map.splitlines():
        if f"`{name}`" in line and "已入权威" in line:
            return True
    return False


def update_skill_map(text: str, rows: list[tuple[str, str, str]]) -> str:
    existing: dict[str, tuple[str, str]] = {}
    if MAP_BEGIN in text and MAP_END in text:
        inner = text.split(MAP_BEGIN, 1)[1].split(MAP_END, 1)[0]
        for line in inner.splitlines():
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cols) >= 3 and cols[0] not in {"name", ""} and not set(cols[0]) <= {"-"}:
                existing[cols[0].strip("`")] = (cols[1], cols[2])
    for name, path, status in rows:
        existing[name] = (path, status)
    body = ["", "| name | 路径 | 状态 |", "|------|------|------|"]
    for name in sorted(existing):
        path, status = existing[name]
        body.append(f"| `{name}` | `{path}` | {status} |")
    body.append("")
    block = MAP_BEGIN + "\n" + "\n".join(body) + "\n" + MAP_END
    if MAP_BEGIN in text and MAP_END in text:
        pre = text.split(MAP_BEGIN, 1)[0]
        post = text.split(MAP_END, 1)[1]
        return pre + block + post
    return text.rstrip() + "\n\n" + block + "\n"


def append_ledger(path: Path, row: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "kind",
        "id",
        "started_at",
        "ended_at",
        "duration_s",
        "tokens_in",
        "tokens_out",
        "tokens_source",
        "model",
        "skills_promoted",
        "notes",
    ]
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in fields})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--digest-ref", default=DIGEST_REF_DEFAULT)
    ap.add_argument("--started-at", default="")
    ap.add_argument("--model", default=os.environ.get("CURSOR_MODEL", "unobserved"))
    ap.add_argument("--session-id", default=os.environ.get("CURSOR_SESSION_ID", ""))
    args = ap.parse_args()

    root = Path(args.root).resolve()
    started = (
        dt.datetime.fromisoformat(args.started_at.replace("Z", "+00:00"))
        if args.started_at
        else utc_now()
    )
    if started.tzinfo is None:
        started = started.replace(tzinfo=dt.timezone.utc)

    tokens_in = os.environ.get("CURSOR_TOKENS_IN", "").strip()
    tokens_out = os.environ.get("CURSOR_TOKENS_OUT", "").strip()
    if tokens_in and tokens_out:
        tokens_source = "env"
    else:
        tokens_in = tokens_in or "unobserved"
        tokens_out = tokens_out or "unobserved"
        tokens_source = "unobserved"

    skill_map_path = root / "SKILL_MAP.md"
    skill_map = skill_map_path.read_text(encoding="utf-8") if skill_map_path.exists() else ""

    digest = git_show(root, f"{args.digest_ref}:DIGEST.md")
    promoted: list[tuple[str, str]] = []
    skipped: list[str] = []
    queued: list[str] = []
    digest_note = ""

    if digest is None:
        digest_note = f"读不到 `{args.digest_ref}:DIGEST.md`，本周期不升格。"
    else:
        names = parse_digest_introduces(digest)
        for name in names:
            if len(promoted) >= MAX_PROMOTE:
                queued.append(name)
                continue
            if already_authoritative(skill_map, name):
                skipped.append(f"{name}：已入权威")
                continue
            rel = find_skill_dir(root, args.digest_ref, name)
            if not rel:
                skipped.append(f"{name}：侦察库无 SKILL.md 路径")
                continue
            skill = git_show(root, f"{args.digest_ref}:{rel}/SKILL.md")
            source = git_show(root, f"{args.digest_ref}:{rel}/SOURCE.md")
            if not skill or not source:
                skipped.append(f"{name}：缺 SKILL.md 或 SOURCE.md")
                continue
            if not license_ok(source):
                skipped.append(f"{name}：LICENSE 闸门未过")
                continue
            dest = root / rel
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "SKILL.md").write_text(skill, encoding="utf-8")
            (dest / "SOURCE.md").write_text(source, encoding="utf-8")
            promoted.append((name, rel))

    # rewrite skill map with promoted
    if promoted:
        skill_map = update_skill_map(
            skill_map,
            [(n, p, "已入权威") for n, p in promoted],
        )
        skill_map_path.write_text(skill_map, encoding="utf-8")

    ended = utc_now()
    duration_s = int((ended - started).total_seconds())
    day = ended.date().isoformat()
    report_dir = root / "projects/OrgOps/records/reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"CYCLE-{day}.md"

    promo_lines = "\n".join(f"- `{n}` → `{p}`" for n, p in promoted) or "- （本周期无升格）"
    skip_lines = "\n".join(f"- {s}" for s in skipped) or "- （无）"
    queue_lines = "\n".join(f"- `{n}`" for n in queued) or "- （无）"

    report = f"""# CYCLE {day}

- **环：** OrgOps 长期环（`LOOP.md`）
- **开始：** {started.isoformat()}
- **结束：** {ended.isoformat()}
- **耗时：** {duration_s}s（墙钟）
- **tokens_in / tokens_out：** {tokens_in} / {tokens_out}（来源：{tokens_source}）
- **模型：** {args.model}

## 一屏结论

本周期升格 **{len(promoted)}** 条（上限 {MAX_PROMOTE}）。
{digest_note}

## 已升格

{promo_lines}

## 跳过

{skip_lines}

## 未升格队列（超上限）

{queue_lines}

## 工作流迭代（本周期）

- 升格只拷 SKILL.md + SOURCE.md
- 合 `main` 仍走 PR，不自动 merge
- token 拿不到就如实 `unobserved`，不编数字

## 请昴看

1. 升格名单是否要改闸门
2. 是否在 cursor.com/automations 挂每日提示词（见 LOOP.md）
"""
    report_path.write_text(report, encoding="utf-8")

    ledger = root / "projects/OrgOps/records/metrics/ledger.csv"
    append_ledger(
        ledger,
        {
            "kind": "cycle",
            "id": f"CYCLE-{day}",
            "started_at": started.isoformat(),
            "ended_at": ended.isoformat(),
            "duration_s": str(duration_s),
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "tokens_source": tokens_source,
            "model": args.model,
            "skills_promoted": ",".join(n for n, _ in promoted),
            "notes": digest_note or f"promoted={len(promoted)} queued={len(queued)}",
        },
    )
    if args.session_id:
        sess_raw = os.environ.get("CURSOR_SESSION_STARTED_AT", started.isoformat())
        try:
            ss = dt.datetime.fromisoformat(sess_raw.replace("Z", "+00:00"))
            if ss.tzinfo is None:
                ss = ss.replace(tzinfo=dt.timezone.utc)
            sess_dur = str(int((ended - ss).total_seconds()))
        except ValueError:
            sess_dur = os.environ.get("CURSOR_SESSION_DURATION_S", "")
        append_ledger(
            ledger,
            {
                "kind": "session",
                "id": args.session_id,
                "started_at": sess_raw,
                "ended_at": ended.isoformat(),
                "duration_s": sess_dur,
                "tokens_in": tokens_in,
                "tokens_out": tokens_out,
                "tokens_source": tokens_source,
                "model": args.model,
                "skills_promoted": ",".join(n for n, _ in promoted),
                "notes": "same cloud run; token unobserved unless env set",
            },
        )

    print(report)
    print(f"\nREPORT={report_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
