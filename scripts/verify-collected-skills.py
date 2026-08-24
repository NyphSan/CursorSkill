#!/usr/bin/env python3
"""Verify skills collected on origin/CursorSkillSearch.

Exit 0 if no blocker; 1 if blockers exist. Always writes a markdown report
to records/verify/ unless --stdout-only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ALLOWED_DIRS = ("game-design", "unreal", "ui-design", "2d", "3d", "workflow")
FORBIDDEN = re.compile(
    r"\b(aimbot|wallhack|esp\b|cheat engine|凭证窃取|盗号|外挂)\b",
    re.I,
)
FRONTMATTER = re.compile(r"\A(?:\ufeff)?---\n(.*?)\n---", re.S)
URL_RE = re.compile(r"https?://[^\s)>\"]+")
LICENSE_RE = re.compile(
    r"(MIT|Apache-2\.0|Apache 2|BSD-3|BSD-2|ISC|CC0|CC-BY|GPL-3|GPL-2|MPL-2|"
    r"Unlicense|许可[：:][^\n]+)",
    re.I,
)

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--ref", default="origin/CursorSkillSearch")
    p.add_argument("--spot-check", type=int, default=12)
    p.add_argument("--stdout-only", action="store_true")
    p.add_argument("--report", default="")
    return p.parse_args()


def list_skill_dirs(ref: str) -> list[str]:
    files = git("ls-tree", "-r", "--name-only", ref).splitlines()
    dirs = []
    for f in files:
        if f.endswith("/SKILL.md") and f.startswith("skills/"):
            dirs.append(f[: -len("/SKILL.md")])
    return sorted(dirs)


def show(ref: str, path: str) -> str:
    try:
        return git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return ""


def check_one(ref: str, skill_dir: str) -> dict:
    parts = skill_dir.split("/")
    direction = parts[1] if len(parts) > 1 else ""
    name = parts[2] if len(parts) > 2 else parts[-1]
    skill = show(ref, f"{skill_dir}/SKILL.md")
    source = show(ref, f"{skill_dir}/SOURCE.md")
    issues: list[str] = []
    warns: list[str] = []

    if direction not in ALLOWED_DIRS:
        issues.append(f"方向目录不在允许集: {direction}")
    if not skill.strip():
        issues.append("SKILL.md 缺失或空")
    if not source.strip():
        issues.append("SOURCE.md 缺失或空")

    skill_text = skill.lstrip("\ufeff") if skill else ""
    fm = FRONTMATTER.search(skill_text) if skill_text else None
    fm_name = fm_desc = ""
    if not fm:
        issues.append("SKILL.md 无 YAML frontmatter")
    else:
        try:
            meta = yaml.safe_load(fm.group(1)) or {}
        except yaml.YAMLError as e:
            issues.append(f"frontmatter YAML 无法解析: {e}")
            meta = {}
        if not isinstance(meta, dict):
            issues.append("frontmatter 不是 mapping")
            meta = {}
        fm_name = str(meta.get("name") or "").strip()
        fm_desc = str(meta.get("description") or "").strip()
        if not fm_name:
            issues.append("frontmatter 缺 name")
        elif fm_name != name:
            warns.append(f"name={fm_name} 与目录 {name} 不一致")
        if not fm_desc or len(fm_desc) < 20:
            issues.append("description 过短或缺失")

    if skill and len(skill) > 180_000:
        warns.append(f"SKILL.md 过大 ({len(skill)} bytes)，疑似整仓镜像")
    if skill and FORBIDDEN.search(skill):
        issues.append("SKILL.md 命中外挂/作弊/凭证类禁词")
    if source and FORBIDDEN.search(source):
        issues.append("SOURCE.md 命中外挂/作弊/凭证类禁词")

    urls = URL_RE.findall(source) if source else []
    github_urls = [u.rstrip(".,") for u in urls if "github.com" in u]
    if not github_urls and not urls:
        issues.append("SOURCE.md 无来源 URL")
    if source and not LICENSE_RE.search(source):
        issues.append("SOURCE.md 未写明 LICENSE/许可")

    digest = hashlib.sha256(skill.encode()).hexdigest()[:12] if skill else ""
    return {
        "dir": skill_dir,
        "direction": direction,
        "name": name,
        "fm_name": fm_name,
        "issues": issues,
        "warns": warns,
        "urls": github_urls or urls,
        "sha": digest,
        "skill_bytes": len(skill),
    }


def head_url(url: str, timeout: float = 8.0) -> str:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "CursorSkill-verify"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as e:
        if e.code in (403, 405):
            try:
                req2 = urllib.request.Request(url, method="GET", headers={"User-Agent": "CursorSkill-verify"})
                with urllib.request.urlopen(req2, timeout=timeout) as resp:
                    return str(resp.status)
            except Exception as e2:
                return f"GET-fail:{e2.__class__.__name__}"
        return str(e.code)
    except Exception as e:
        return f"err:{e.__class__.__name__}"


def digest_introduces(ref: str) -> list[str]:
    text = show(ref, "DIGEST.md")
    if not text:
        return []
    names = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("## 建议引入"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if in_table and line.startswith("|") and "名称" not in line and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells:
                names.append(cells[0])
    return names


def render(report: dict) -> str:
    day = report["date"]
    blockers = report["blockers"]
    warns = report["warns"]
    lines = [
        f"# VERIFY {day}",
        "",
        f"- ref: `{report['ref']}` @ `{report['commit'][:12]}`",
        f"- 技能数: **{report['count']}**（SKILL/SOURCE 成对）",
        f"- 阻断: **{len(blockers)}**  警告: **{len(warns)}**",
        f"- 方向分布: {', '.join(f'{k}={v}' for k,v in report['dirs'].items())}",
        f"- DIGEST 建议引入: {', '.join(report['introduces']) or '（无表）'}",
        "",
        "## 一屏结论",
        "",
        report["verdict"],
        "",
        "## 阻断项",
        "",
    ]
    if not blockers:
        lines.append("无。")
    else:
        for b in blockers:
            lines.append(f"- `{b['dir']}`: " + "; ".join(b["issues"]))
    lines += ["", "## 警告", ""]
    if not warns:
        lines.append("无。")
    else:
        for w in warns[:40]:
            lines.append(f"- `{w['dir']}`: " + "; ".join(w["warns"]))
        if len(warns) > 40:
            lines.append(f"- …另有 {len(warns)-40} 条警告未展开")
    lines += ["", "## 来源抽检（HTTP HEAD）", ""]
    if not report["url_checks"]:
        lines.append("本轮未抽检。")
    else:
        for row in report["url_checks"]:
            lines.append(f"- `{row['name']}` {row['url']} → **{row['status']}**")
    lines += ["", "## 重复 name", ""]
    if not report["dupes"]:
        lines.append("无。")
    else:
        for n, paths in report["dupes"].items():
            lines.append(f"- `{n}`: " + ", ".join(f"`{p}`" for p in paths))
    lines += ["", "## 未覆盖", "",
              "- 不执行 skill 内脚本，不做运行时功能测试。",
              "- 不把 CursorSkillSearch 合进 main。",
              "- 来源 URL 只抽检 DIGEST 引入 + 随机样本。",
              ""]
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    ref = args.ref
    try:
        git("rev-parse", ref)
    except subprocess.CalledProcessError:
        git("fetch", "origin", ref.split("/", 1)[-1])
    commit = git("rev-parse", ref)
    dirs = list_skill_dirs(ref)
    results = [check_one(ref, d) for d in dirs]
    blockers = [r for r in results if r["issues"]]
    warns = [r for r in results if r["warns"] and not r["issues"]]
    dir_counts = Counter(r["direction"] for r in results)
    by_name: dict[str, list[str]] = defaultdict(list)
    for r in results:
        key = r["fm_name"] or r["name"]
        by_name[key].append(r["dir"])
    dupes = {k: v for k, v in by_name.items() if len(v) > 1}
    introduces = digest_introduces(ref)

    spot_names = list(introduces)
    remaining = [r for r in results if r["name"] not in spot_names and r["urls"]]
    remaining.sort(key=lambda r: r["dir"])
    for r in remaining:
        if len(spot_names) >= args.spot_check:
            break
        spot_names.append(r["name"])
    url_checks = []
    wanted = {n for n in spot_names}
    for r in results:
        if r["name"] not in wanted or not r["urls"]:
            continue
        status = head_url(r["urls"][0])
        url_checks.append({"name": r["name"], "url": r["urls"][0], "status": status})
        if len(url_checks) >= args.spot_check:
            break

    dead = [u for u in url_checks if u["status"] not in {"200", "301", "302"}]
    # Duplicate YAML names are expected when vendors are namespaced by folder.
    if dupes:
        for n, paths in dupes.items():
            warns.append({"dir": n, "warns": [f"重复 name → {', '.join(paths)}"], "issues": []})
    if blockers or dead:
        verdict = "未通过：存在结构阻断或失效来源，需人工看阻断项。"
    elif warns:
        verdict = "有条件通过：结构完整，但有 name/体积/重名警告，下一轮优先处理。"
    else:
        verdict = "通过：成对 SKILL+SOURCE、方向合法、抽检来源可访问。"

    report = {
        "date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
        "ref": ref,
        "commit": commit,
        "count": len(results),
        "dirs": dict(dir_counts),
        "blockers": blockers,
        "warns": warns,
        "dupes": dupes,
        "introduces": introduces,
        "url_checks": url_checks,
        "verdict": verdict,
    }
    md = render(report)
    if not args.stdout_only:
        out = Path(args.report) if args.report else ROOT / "records" / "verify" / f"VERIFY-{report['date']}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        latest = ROOT / "records" / "verify" / "LATEST.md"
        latest.write_text(md, encoding="utf-8")
        print(f"wrote {out}", file=sys.stderr)
    sys.stdout.write(md)
    return 1 if (blockers or dead) else 0


if __name__ == "__main__":
    os.chdir(ROOT)
    sys.exit(main())
