"""
tests/test_skill_contract.py
----------------------------
Contract of the public skill: frontmatter, size, local links, no vendor tokens.
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "energyincloud"
SKILL = SKILL_DIR / "SKILL.md"

# Copied from triage-api origin/stage src/app/knowledge/build.py (VENDOR_TOKENS, the I5 dictionary).
VENDOR_TOKENS = (
    "Acrel", "Chint", "Deye", "Eastron", "EBM-PAPST", "Envicool", "Fronius", "Gavazzi",
    "Growatt", "Huawei", "Inim", "Livoltek", "Pylontech", "Schneider Electric", "Senergy",
    "Sermatec", "Sinexcel", "SMA", "SolarEdge", "Solis", "Sungrow", "Sunmeter",
    "Thytronic", "USR IOT", "Weidmüller",
)
VENDOR_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(t) for t in sorted(VENDOR_TOKENS)) + r")\b", re.IGNORECASE
)


def _frontmatter_keys(text: str) -> set[str]:
    lines = text.splitlines()
    assert lines[0] == "---", "SKILL.md must open with a frontmatter fence"
    end = lines.index("---", 1)
    return {m.group(1) for line in lines[1:end] if (m := re.match(r"^([A-Za-z_-]+):", line))}


def _public_texts() -> list[Path]:
    return sorted(SKILL_DIR.rglob("*.md")) + [ROOT / "README.md"]


def test_frontmatter_keys_exactly_name_and_description():
    assert _frontmatter_keys(SKILL.read_text(encoding="utf-8")) == {"name", "description"}


def test_skill_under_500_lines():
    assert len(SKILL.read_text(encoding="utf-8").splitlines()) < 500


def test_local_links_resolve():
    text = SKILL.read_text(encoding="utf-8")
    md_links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text)
    code_paths = re.findall(r"`(references/[^`\s]+)`", text)
    targets = [t for t in md_links if not re.match(r"^[a-z]+:", t)] + code_paths
    assert code_paths, "SKILL.md is expected to reference its references/ files"
    missing = [t for t in targets if not (SKILL_DIR / t).is_file()]
    assert not missing, f"unresolved links: {missing}"


@pytest.mark.parametrize("path", _public_texts(), ids=lambda p: str(p.relative_to(ROOT)))
def test_no_vendor_tokens(path: Path):
    hits = VENDOR_RE.findall(path.read_text(encoding="utf-8"))
    assert not hits, f"vendor tokens in {path.name}: {hits}"
