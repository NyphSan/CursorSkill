#!/usr/bin/env python3
"""Verify skills collected on origin/CursorSkillSearch.

Exit 0 if no blocker; 1 if blockers exist. Always writes a markdown report
to records/verify/ unless --stdout-only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ALLOWED_DIRS = ("game-design", "unreal", "ui-design", "2d", "3d", "workflow")
TARGET_HINTS = {
    "game-design": re.compile(
        r"game|gameplay|gdd|narrative|combat|economy|level.?design|quest|player|mechanics",
        re.I,
    ),
    "unreal": re.compile(
        r"unreal|ue5|ue4|\bue\b|umg|niagara|replication|blueprint|gas\b|gameplay.?ability",
        re.I,
    ),
    "ui-design": re.compile(r"\bui\b|\bux\b|hud|widget|interface|figma|layout|visual design", re.I),
    "2d": re.compile(r"\b2d\b|sprite|pixel|isometric|tileset|tilemap|canvas", re.I),
    "3d": re.compile(r"\b3d\b|blender|maya|houdini|mesh|\blod\b|nanite|skeletal", re.I),
    "workflow": re.compile(r"pipeline|workflow|review|\bci\b|\bgit\b|process|playtest|\bqa\b", re.I),
}
FORBIDDEN = re.compile(
    r"\b(aimbot|wallhack|esp\b|cheat engine|凭证窃取|盗号|外挂)\b",
    re.I,
)
FRONTMATTER = re.compile(r"\A(?:\ufeff)?---\r?\n(.*?)\r?\n---", re.S)
NAME_LINE = re.compile(r"^name:\s*[\"']?([^\"'\n]+)", re.M)
DESC_LINE = re.compile(r"^description:\s*[\"']?(.*)$", re.M)
URL_RE = re.compile(r"https://github.com/[\w.-]+/[\w.-]+")
LICENSE_RE = re.compile(
    r"(MIT|Apache-2\.0|Apache 2|BSD-3|BSD-2|ISC|CC0|CC-BY|GPL-3|GPL-2|MPL-2|"
    r"Unlicense|许可[：:][^\n]+)",
    re.I,
)

ROOT = Path(__file__).resolve().parents[1]


def is_vendor_namespaced(dir_name: str, fm_name: str) -> bool:
    """True when folder is `{vendor}-{name}` and frontmatter name is `{name}`."""
    if not dir_name or not fm_name or dir_name == fm_name:
        return False
    return dir_name.endswith("-" + fm_name)


def parse_skill_yaml(raw: str) -> tuple[dict, str | None]:
    """Parse YAML frontmatter body. Error is 'yaml-unquoted-colon' on YAMLError."""
    try:
        meta = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return {}, "yaml-unquoted-colon"
    if not isinstance(meta, dict):
        return {}, "frontmatter-not-mapping"
    return meta, None


def suggested_yaml(name: str, desc: str) -> str:
    """Quote-safe frontmatter: description as a `|` block."""
    indented = "\n".join(("  " + ln) if ln else "  " for ln in (desc or "").splitlines())
    return f"---\nname: {name}\ndescription: |\n{indented}\n---"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--ref", default="origin/CursorSkillSearch")
    p.add_argument("--spot-check", type=int, default=0, help="0 = HEAD 全部独立 github 来源")
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


def normalize_license(raw: str) -> str:
    s = raw.strip()
    if re.search(r"未声明|无 LICENSE|NOASSERTION|未明示", s, re.I):
        return "未声明/待核"
    m = re.search(
        r"(Apache-2\.0|MIT|BSD-3|BSD-2|ISC|CC0|CC-BY|GPL-3|GPL-2|MPL-2|Unlicense)",
        s,
        re.I,
    )
    if m:
        tok = m.group(1)
        return "MIT" if tok.lower() == "mit" else tok
    if "原仓" in s or "原仓库" in s:
        return "见原仓 LICENSE"
    return s[:48] or "（未写明）"


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
    yaml_ok = False
    ns_name = False
    if not fm:
        issues.append("SKILL.md 无 YAML frontmatter")
    else:
        raw = fm.group(1)
        meta, yaml_err = parse_skill_yaml(raw)
        if yaml_err == "yaml-unquoted-colon":
            issues.append(
                "yaml-unquoted-colon：description 含未加引号的冒号，标准 YAML 失败；"
                "Cursor 加载该 skill 也可能失败"
            )
            nm = NAME_LINE.search(raw)
            ds = DESC_LINE.search(raw)
            if nm:
                fm_name = nm.group(1).strip()
            if ds:
                fm_desc = ds.group(1).strip().strip("\"'")
        elif yaml_err == "frontmatter-not-mapping":
            issues.append("frontmatter 不是 mapping")
        else:
            yaml_ok = True
            fm_name = str(meta.get("name") or "").strip()
            fm_desc = str(meta.get("description") or "").strip()
        ns_name = is_vendor_namespaced(name, fm_name)
        if not fm_name:
            issues.append("frontmatter 缺 name")
        elif fm_name != name and not ns_name:
            warns.append(f"name={fm_name} 与目录 {name} 不一致")
        if yaml_ok and (not fm_desc or len(fm_desc) < 20):
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
    license_name = ""
    lm = re.search(r"许可[：:]\s*([^\n]+)", source or "")
    if lm:
        license_name = normalize_license(lm.group(1))
    elif source and LICENSE_RE.search(source):
        license_name = normalize_license(LICENSE_RE.search(source).group(1))
    if source and not license_name:
        issues.append("SOURCE.md 未写明 LICENSE/许可")

    blob = f"{fm_desc}\n{skill[:2500]}\n{source[:800]}"
    hint = TARGET_HINTS.get(direction)
    yaml_broken = any("yaml-unquoted-colon" in i for i in issues)
    target_miss = bool(hint and not yaml_broken and not hint.search(blob))
    if target_miss:
        warns.append("目标命中弱：描述/正文未出现本方向关键词")

    digest = hashlib.sha256(skill.encode()).hexdigest()[:12] if skill else ""
    return {
        "dir": skill_dir,
        "direction": direction,
        "name": name,
        "fm_name": fm_name,
        "fm_desc": fm_desc,
        "issues": issues,
        "warns": warns,
        "urls": github_urls or urls,
        "license": license_name,
        "target_miss": target_miss,
        "sha": digest,
        "skill_bytes": len(skill),
        "ns_name": ns_name,
    }


def head_url(url: str, timeout: float = 8.0) -> str:
    url = URL_RE.search(url).group(0) if URL_RE.search(url) else url
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


REPO_RE = re.compile(r"https://github.com/([\w.-]+)/([\w.-]+)")


def _gh_api_json(path: str) -> tuple[int, dict]:
    """Authenticated GitHub REST via `gh`. Returns (status, payload)."""
    proc = subprocess.run(
        ["gh", "api", "-H", "Accept: application/vnd.github+json", path],
        capture_output=True,
        text=True,
    )
    body = proc.stdout or ""
    try:
        data = json.loads(body) if body.lstrip().startswith("{") else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        data = {}
    if proc.returncode == 0:
        return 200, data
    status = data.get("status")
    if status:
        try:
            return int(status), data
        except (TypeError, ValueError):
            pass
    err = (proc.stderr or "") + body
    if "404" in err or "Not Found" in err:
        return 404, data
    if "403" in err:
        return 403, data
    return 1, data


def verdict_from_license_payload(url: str, repo: str, data: dict) -> dict:
    spdx = (data.get("license") or {}).get("spdx_id") or ""
    html = data.get("html_url") or ""
    if spdx and spdx not in {"NOASSERTION", "NONE"}:
        return {"url": url, "repo": repo, "verdict": f"GitHub SPDX={spdx}", "html": html}
    raw = data.get("download_url") or ""
    text = ""
    if raw:
        try:
            req = urllib.request.Request(raw, headers={"User-Agent": "CursorSkill-verify"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                text = resp.read(800).decode("utf-8", "replace")
        except Exception:
            text = ""
    if re.search(r"MIT License", text, re.I):
        return {"url": url, "repo": repo, "verdict": "文件是 MIT，GitHub SPDX=NOASSERTION", "html": html}
    if re.search(r"Apache License", text, re.I):
        return {"url": url, "repo": repo, "verdict": "文件是 Apache-2.0，GitHub SPDX=NOASSERTION", "html": html}
    return {"url": url, "repo": repo, "verdict": f"有 LICENSE 文件但 SPDX={spdx or '未知'}", "html": html}


def probe_github_license(url: str) -> dict:
    m = REPO_RE.search(url or "")
    if not m:
        return {"url": url, "repo": "", "verdict": "无法解析仓库"}
    repo = f"{m.group(1)}/{m.group(2)}"
    status: int | None = None
    data: dict = {}
    try:
        status, data = _gh_api_json(f"repos/{repo}/license")
    except FileNotFoundError:
        status = None
    if status is None:
        api = f"https://api.github.com/repos/{repo}/license"
        req = urllib.request.Request(
            api, headers={"User-Agent": "CursorSkill-verify", "Accept": "application/vnd.github+json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                status = 200
        except urllib.error.HTTPError as e:
            status = e.code
        except Exception as e:
            return {"url": url, "repo": repo, "verdict": f"err:{e.__class__.__name__}", "html": f"https://github.com/{repo}"}
    if status == 404:
        return {"url": url, "repo": repo, "verdict": "原仓无 GitHub 可识别 LICENSE（404）", "html": f"https://github.com/{repo}"}
    if status != 200:
        return {"url": url, "repo": repo, "verdict": f"api err {status}", "html": f"https://github.com/{repo}"}
    return verdict_from_license_payload(url, repo, data)


def unique_github_urls(results: list[dict]) -> list[tuple[str, str]]:
    seen: dict[str, str] = {}
    for r in results:
        for u in r["urls"]:
            if "github.com" not in u:
                continue
            key = "/".join(u.rstrip("/").split("/")[:5])
            if key not in seen:
                seen[key] = r["name"]
    return sorted((url, name) for url, name in seen.items())


def head_unique_urls(pairs: list[tuple[str, str]], limit: int) -> list[dict]:
    chosen = pairs if limit == 0 else pairs[:limit]
    out = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(head_url, url): (url, name) for url, name in chosen}
        for fut in as_completed(futs):
            url, name = futs[fut]
            out.append({"name": name, "url": url, "status": fut.result()})
    out.sort(key=lambda r: r["url"])
    return out


def append_runlog(
    report: dict,
    commit: str,
    blockers: list[dict],
    warns: list[dict],
    verdict: str,
) -> None:
    runlog = ROOT / "records" / "verify" / "RUNLOG.md"
    header = (
        "# 验证环 RUNLOG\n\n"
        "每次抽检追加一行。侦察分支没变时也能看出日跑有没有执行。\n\n"
        "| 时刻 (UTC) | ref | 技能 | 阻断 | 警告 | 结论 |\n"
        "|---|---|---:|---:|---:|---|\n"
    )
    short = verdict.replace("|", "/").split("。")[0]
    row = (
        f"| {report['verified_at']} | `{commit[:12]}` | {report['count']} | "
        f"{len(blockers)} | {len(warns)} | {short} |\n"
    )
    if not runlog.exists():
        runlog.write_text(header + row, encoding="utf-8")
        return
    text = runlog.read_text(encoding="utf-8")
    if "| 时刻 (UTC) |" not in text:
        runlog.write_text(header + row, encoding="utf-8")
        return
    runlog.write_text(text.rstrip() + "\n" + row, encoding="utf-8")


HEAD_ROW = re.compile(
    r"^- `[^`]+` (https://github\.com/\S+) → \*\*(\S+)\*\*"
)
OK_HEAD = {"200", "301", "302"}


def previous_blockers() -> set[str]:
    latest = ROOT / "records" / "verify" / "LATEST.md"
    if not latest.exists():
        return set()
    found = set()
    in_block = False
    for line in latest.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 阻断项"):
            in_block = True
            continue
        if in_block and line.startswith("## "):
            break
        if in_block and line.startswith("- `skills/"):
            found.add(line.split("`")[1])
    return found


def previous_dead() -> set[str]:
    """Repo URLs whose last LATEST 来源抽检 status was not 2xx/3xx."""
    latest = ROOT / "records" / "verify" / "LATEST.md"
    if not latest.exists():
        return set()
    found = set()
    in_src = False
    for line in latest.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 来源抽检"):
            in_src = True
            continue
        if in_src and line.startswith("## "):
            break
        if not in_src:
            continue
        m = HEAD_ROW.match(line)
        if m and m.group(2) not in OK_HEAD:
            found.add(m.group(1))
    return found


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
        f"- 抽检时刻: `{report['verified_at']}`",
        f"- 技能数: **{report['count']}**（SKILL/SOURCE 成对）",
        f"- 阻断: **{len(blockers)}**  警告: **{len(warns)}**",
        f"- 供应商前缀命名: {report.get('ns_name_n', 0)}（name 与目录后缀一致，不计入警告）",
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
    lines += ["", "## 许可分布", ""]
    if not report["licenses"]:
        lines.append("无。")
    else:
        for k, v in report["licenses"].items():
            lines.append(f"- {k}: {v}")
    pending_n = report["licenses"].get("未声明/待核", 0)
    if pending_n:
        lines.append(f"未声明/待核 {pending_n} 条已写入 `records/verify/ESCALATION.md`，升格前先核原仓 LICENSE。")
    lines += ["", "## 许可原仓探测", ""]
    if not report.get("license_probes"):
        lines.append("本轮无待核许可可探测。")
    else:
        for p in report["license_probes"]:
            lines.append(f"- `{p.get('repo') or p.get('url')}`：{p.get('verdict')}")
    lines += ["", "## 目标命中", ""]
    misses = report.get("target_misses") or []
    if not misses:
        lines.append("抽检范围内未见方向关键词空缺。")
    else:
        lines.append(f"{len(misses)} 条目录方向与正文关键词对不上（警告，不阻断）：")
        for m in misses[:20]:
            lines.append(f"- `{m}`")
        if len(misses) > 20:
            lines.append(f"- …另有 {len(misses)-20} 条")
    lines += ["", "## DIGEST 引入是否在库里", ""]
    if not report["introduces"]:
        lines.append("DIGEST 无引入表。")
    elif not report["missing_introduces"]:
        lines.append("建议引入项都能在 `skills/` 下找到同名目录。")
    else:
        lines.append("下列 DIGEST 引入在侦察库找不到目录：")
        for n in report["missing_introduces"]:
            lines.append(f"- `{n}`")
    lines += ["", "## 相对上次差量", ""]
    lines.append(report["delta"] or "无上次报告可比。")
    lines += ["", "## 来源抽检（HTTP HEAD，独立仓库）", ""]
    if not report["url_checks"]:
        lines.append("本轮未抽检。")
    else:
        dead_rows = [row for row in report["url_checks"] if row["status"] not in OK_HEAD]
        ok_n = len(report["url_checks"]) - len(dead_rows)
        lines.append(f"独立来源 {len(report['url_checks'])}，可访问 {ok_n}，失效 {len(dead_rows)}。")
        show_rows = dead_rows or report["url_checks"][:12]
        for row in show_rows:
            lines.append(f"- `{row['name']}` {row['url']} → **{row['status']}**")
        if not dead_rows and len(report["url_checks"]) > 12:
            lines.append(f"- …其余 {len(report['url_checks'])-12} 条均为 2xx/3xx")
    lines += ["", "## 重复 name", ""]
    if not report["dupes"]:
        lines.append("无。")
    else:
        for n, paths in report["dupes"].items():
            lines.append(f"- `{n}`: " + ", ".join(f"`{p}`" for p in paths))
    lines += ["", "## 升级给昴", ""]
    yaml_blockers = [
        b for b in blockers if any("yaml-unquoted-colon" in i for i in b["issues"])
    ]
    dead_rows = [
        row
        for row in report.get("url_checks") or []
        if row["status"] not in OK_HEAD
    ]
    wrote_upgrade = False
    if yaml_blockers:
        lines.append(
            f"这 {len(yaml_blockers)} 条 skill 的 description 没加引号又含冒号，YAML 非法。"
            "修复：把 description 改成 `|` 或多行引号。"
        )
        lines.append("不在验证环里直接改侦察分支，避免和 SkillSearch 抢写。")
        for b in yaml_blockers:
            lines.append(f"- `{b['dir']}`")
        wrote_upgrade = True
    if dead_rows:
        if wrote_upgrade:
            lines.append("")
        lines.append(
            f"失效来源 {len(dead_rows)} 个：原仓 HEAD 非 2xx/3xx。升格应拦；验证环不改侦察分支。"
        )
        for row in dead_rows:
            lines.append(f"- `{row['name']}` {row['url']} → **{row['status']}**")
        wrote_upgrade = True
    if not wrote_upgrade:
        if blockers:
            lines.append("见上方阻断项，需人工决定修、降级还是移出侦察库。")
        else:
            lines.append("无阻断，不必升级。")
    lines += ["", "## 未覆盖", "",
              "- 不执行 skill 内脚本，不做运行时功能测试。",
              "- 不把 CursorSkillSearch 合进 main。",
              "- 来源 URL 对独立 github 仓库做 HEAD；同一仓下多条 skill 不重复打。",
              ""]
    return "\n".join(lines) + "\n"


def dirs_for_repo_url(results: list[dict], url: str) -> list[str]:
    key = "/".join((url or "").rstrip("/").split("/")[:5])
    found: list[str] = []
    for r in results:
        for u in r.get("urls") or []:
            if "/".join(u.rstrip("/").split("/")[:5]) == key:
                found.append(r["dir"])
                break
    return found


def build_escalation(
    date: str,
    yaml_blockers: list[dict],
    pending: list[dict],
    license_probes: list[dict],
    misses: list[str],
    dead_rows: list[dict],
    results: list[dict],
) -> str | None:
    """Markdown for ESCALATION.md, or None when there is nothing to escalate."""
    if not (yaml_blockers or pending or misses or dead_rows):
        return None
    esc_lines = [f"# 升级 · {date}", ""]
    if yaml_blockers:
        esc_lines += [
            "给昴：以下 skill 的 YAML frontmatter 非法，加载可能失败。",
            "验证环不直接改 `CursorSkillSearch`，避免和 SkillSearch 抢写。",
            "建议：把 description 改成 `|` 块或整段加引号。",
            "",
        ]
        for b in yaml_blockers:
            esc_lines.append(f"- `{b['dir']}`")
        esc_lines += [
            "",
            "## 可贴修法（验证环不改侦察分支）",
            "",
            "把 `description:` 改成 `|` 块。下面已用标准 YAML 可解析的写法列出，给 SkillSearch 下次入库或昴在侦察分支手改。",
            "",
        ]
        for b in yaml_blockers:
            esc_lines += [
                f"### `{b['dir']}/SKILL.md`",
                "",
                "```yaml",
                suggested_yaml(b.get("fm_name") or b.get("name") or "", b.get("fm_desc") or ""),
                "```",
                "",
            ]
    if dead_rows:
        esc_lines += [
            "## 失效来源（HEAD 非 2xx/3xx）",
            "",
            "原仓 URL 已不可访问。验证环不改 `CursorSkillSearch`。升格进权威库应拦下；SkillSearch 下次入库应改 SOURCE 或移出。",
            "",
        ]
        for row in dead_rows:
            dirs = dirs_for_repo_url(results, row.get("url") or "")
            label = ", ".join(f"`{d}`" for d in dirs) or f"`{row.get('name')}`"
            esc_lines.append(
                f"- {label} — {row.get('url')} → **{row.get('status')}**"
            )
        esc_lines.append("")
    if pending:
        probe_by_url = {p.get("url"): p for p in license_probes}
        esc_lines += [
            "许可待核。下面是本轮对原仓 GitHub license API 的探测结果。",
            "无 LICENSE 的仓，升格进权威库应拦下；有文件但 SPDX=NOASSERTION 的，SOURCE 可改记实际许可证。",
            "",
        ]
        for r in pending:
            u = (r["urls"] or [""])[0]
            probe = probe_by_url.get(u) or {}
            esc_lines.append(f"- `{r['dir']}` — {u} — {probe.get('verdict', '未探测')}")
        esc_lines.append("")
    if misses:
        esc_lines += [
            "目标命中弱（目录方向和正文关键词对不上，警告不阻断）：",
            "",
        ]
        for d in misses[:20]:
            esc_lines.append(f"- `{d}`")
        if len(misses) > 20:
            esc_lines.append(f"- …另有 {len(misses)-20} 条")
        esc_lines.append("")
    return "\n".join(esc_lines)


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
    names_on_disk = {r["name"] for r in results}
    missing_introduces = [n for n in introduces if n not in names_on_disk]
    licenses = Counter((r.get("license") or "（未写明）") for r in results)
    prev = previous_blockers()
    prev_dead = previous_dead()
    now_block = {b["dir"] for b in blockers}
    added = sorted(now_block - prev)
    gone = sorted(prev - now_block)
    has_latest = (ROOT / "records" / "verify" / "LATEST.md").exists()

    url_checks = head_unique_urls(unique_github_urls(results), args.spot_check)
    dead = [u for u in url_checks if u["status"] not in OK_HEAD]
    now_dead = {u["url"] for u in dead}
    dead_added = sorted(now_dead - prev_dead)
    dead_gone = sorted(prev_dead - now_dead)
    if has_latest:
        delta = (
            f"新增阻断 {len(added)}：{', '.join(f'`{x}`' for x in added) or '无'}；"
            f"消失 {len(gone)}：{', '.join(f'`{x}`' for x in gone) or '无'}。"
            f" 失效来源新增 {len(dead_added)}：{', '.join(f'`{x}`' for x in dead_added) or '无'}；"
            f"消失 {len(dead_gone)}：{', '.join(f'`{x}`' for x in dead_gone) or '无'}。"
        )
    else:
        delta = "无上次报告可比。"
    pending = [r for r in results if r.get("license") == "未声明/待核"]
    pending_repos: dict[str, dict] = {}
    for r in pending:
        u = (r["urls"] or [""])[0]
        if u not in pending_repos:
            pending_repos[u] = probe_github_license(u)
    license_probes = list(pending_repos.values())
    # Duplicate YAML names are expected when vendors are namespaced by folder.
    if dupes:
        for n, paths in dupes.items():
            warns.append({"dir": n, "warns": [f"重复 name → {', '.join(paths)}"], "issues": []})
    fail_bits = []
    if blockers:
        fail_bits.append(f"{len(blockers)} 条结构阻断")
    if dead:
        fail_bits.append(f"{len(dead)} 个失效来源")
    if missing_introduces:
        fail_bits.append("DIGEST 引入不在库中")
    if fail_bits:
        verdict = "未通过：" + "，".join(fail_bits) + "。"
    elif warns:
        verdict = "有条件通过：结构完整，但有 name/体积/重名警告，下一轮优先处理。"
    else:
        verdict = "通过：成对 SKILL+SOURCE、方向合法、抽检来源可访问。"

    report = {
        "date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
        "verified_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ref": ref,
        "commit": commit,
        "count": len(results),
        "dirs": dict(dir_counts),
        "blockers": blockers,
        "warns": warns,
        "dupes": dupes,
        "introduces": introduces,
        "url_checks": url_checks,
        "licenses": dict(licenses.most_common()),
        "missing_introduces": missing_introduces,
        "delta": delta,
        "license_probes": license_probes,
        "target_misses": [r["dir"] for r in results if r.get("target_miss")],
        "ns_name_n": sum(1 for r in results if r.get("ns_name")),
        "verdict": verdict,
    }
    md = render(report)
    if not args.stdout_only:
        out = Path(args.report) if args.report else ROOT / "records" / "verify" / f"VERIFY-{report['date']}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md, encoding="utf-8")
        latest = ROOT / "records" / "verify" / "LATEST.md"
        latest.write_text(md, encoding="utf-8")
        esc = ROOT / "records" / "verify" / "ESCALATION.md"
        yaml_blockers = [
            b for b in blockers if any("yaml-unquoted-colon" in i for i in b["issues"])
        ]
        pending = [r for r in results if r.get("license") == "未声明/待核"]
        misses = [r["dir"] for r in results if r.get("target_miss")]
        esc_md = build_escalation(
            report["date"],
            yaml_blockers,
            pending,
            license_probes,
            misses,
            dead,
            results,
        )
        if esc_md:
            esc.write_text(esc_md, encoding="utf-8")
        append_runlog(report, commit, blockers, warns, verdict)
        print(f"wrote {out}", file=sys.stderr)
    sys.stdout.write(md)
    return 1 if (blockers or dead or missing_introduces) else 0


if __name__ == "__main__":
    os.chdir(ROOT)
    sys.exit(main())
