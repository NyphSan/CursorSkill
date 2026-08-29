#!/usr/bin/env python3
"""Self-tests for the collected-skills verifier. No scout-branch / network."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "verify-collected-skills.py"


def load_mod():
    spec = importlib.util.spec_from_file_location("verify_collected_skills", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class VendorName(unittest.TestCase):
    def setUp(self) -> None:
        self.m = load_mod()

    def test_vendor_prefix(self) -> None:
        self.assertTrue(
            self.m.is_vendor_namespaced("heycat-animated-sprite-generation", "animated-sprite-generation")
        )
        self.assertTrue(self.m.is_vendor_namespaced("omer-concept-art", "concept-art"))
        self.assertFalse(self.m.is_vendor_namespaced("concept-art", "concept-art"))
        self.assertFalse(self.m.is_vendor_namespaced("foo", "bar"))
        self.assertFalse(self.m.is_vendor_namespaced("", "x"))


class YamlFrontmatter(unittest.TestCase):
    def setUp(self) -> None:
        self.m = load_mod()

    def test_unquoted_colon(self) -> None:
        raw = "name: omer-concept-art\ndescription: Use this: when drawing\n"
        meta, err = self.m.parse_skill_yaml(raw)
        self.assertEqual(err, "yaml-unquoted-colon")
        self.assertEqual(meta, {})

    def test_quoted_colon_ok(self) -> None:
        raw = 'name: omer-concept-art\ndescription: "Use this: when drawing concept art"\n'
        meta, err = self.m.parse_skill_yaml(raw)
        self.assertIsNone(err)
        self.assertEqual(meta["name"], "omer-concept-art")

    def test_block_scalar_ok(self) -> None:
        raw = "name: foo\ndescription: |\n  Use this: when drawing\n"
        meta, err = self.m.parse_skill_yaml(raw)
        self.assertIsNone(err)
        self.assertIn("when drawing", meta["description"])

    def test_suggested_yaml_parses_colon(self) -> None:
        blob = self.m.suggested_yaml("concept-art", "Use this: when drawing")
        body = "\n".join(blob.splitlines()[1:-1])
        meta, err = self.m.parse_skill_yaml(body)
        self.assertIsNone(err)
        self.assertEqual(meta["name"], "concept-art")
        self.assertIn("when drawing", meta["description"])


class LicenseNorm(unittest.TestCase):
    def setUp(self) -> None:
        self.m = load_mod()

    def test_mit(self) -> None:
        self.assertEqual(self.m.normalize_license("MIT"), "MIT")

    def test_pending(self) -> None:
        self.assertEqual(self.m.normalize_license("未声明"), "未声明/待核")

    def test_upstream(self) -> None:
        self.assertEqual(self.m.normalize_license("见原仓 LICENSE"), "见原仓 LICENSE")

    def test_verdict_spdx(self) -> None:
        out = self.m.verdict_from_license_payload(
            "https://github.com/o/r",
            "o/r",
            {"license": {"spdx_id": "MIT"}, "html_url": "https://github.com/o/r/LICENSE"},
        )
        self.assertEqual(out["verdict"], "GitHub SPDX=MIT")


class Runlog(unittest.TestCase):
    def test_append_and_blockers(self) -> None:
        m = load_mod()
        tmp = Path(tempfile.mkdtemp())
        (tmp / "records" / "verify").mkdir(parents=True)
        m.ROOT = tmp
        latest = tmp / "records" / "verify" / "LATEST.md"
        latest.write_text(
            "## 阻断项\n\n- `skills/2d/omer-concept-art`: yaml-unquoted-colon\n\n## 警告\n\n无。\n",
            encoding="utf-8",
        )
        self.assertEqual(m.previous_blockers(), {"skills/2d/omer-concept-art"})
        report = {"verified_at": "2026-08-24T05:00:00Z", "count": 322}
        m.append_runlog(report, "aa2d7074e7ad", [{"dir": "a"}] * 8, [{"dir": "w"}], "未通过：8 条结构阻断。")
        text = (tmp / "records" / "verify" / "RUNLOG.md").read_text(encoding="utf-8")
        self.assertIn("| 2026-08-24T05:00:00Z |", text)
        self.assertIn("未通过：8 条结构阻断", text)


class Escalation(unittest.TestCase):
    def test_dead_source_section(self) -> None:
        m = load_mod()
        text = m.build_escalation(
            date="2026-08-29",
            yaml_blockers=[],
            pending=[],
            license_probes=[],
            misses=[],
            dead_rows=[
                {
                    "name": "arg-games-unreal-cqtest",
                    "url": "https://github.com/arg-games/Unreal-Skill",
                    "status": "404",
                }
            ],
            results=[
                {
                    "dir": "skills/unreal/arg-games-unreal-cqtest",
                    "urls": ["https://github.com/arg-games/Unreal-Skill"],
                }
            ],
        )
        self.assertIsNotNone(text)
        assert text is not None
        self.assertIn("失效来源", text)
        self.assertIn("skills/unreal/arg-games-unreal-cqtest", text)
        self.assertIn("https://github.com/arg-games/Unreal-Skill", text)
        self.assertIn("404", text)

    def test_empty_returns_none(self) -> None:
        m = load_mod()
        self.assertIsNone(
            m.build_escalation("2026-08-29", [], [], [], [], [], [])
        )


if __name__ == "__main__":
    unittest.main()
