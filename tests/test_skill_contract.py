"""
tests/test_skill_contract.py
----------------------------
Contract of the public skills and the Copilot agent instructions: frontmatter, size, local
links, no vendor tokens, and byte identity with the generated tree in triage-api
(`plugins/energyincloud/`) when that checkout sits next to this repository.
"""
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / "commands"
COPILOT_INSTRUCTIONS = ROOT / "copilot" / "appPackage" / "instruction.txt"
SKILLS = sorted(p for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").is_file())
# The generated tree these files are copied from; absent on a clone without the sibling.
GENERATED = ROOT.parent / "triage-api" / "plugins" / "energyincloud"

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
    return (
        sorted(ROOT.glob("skills/**/*.md"))
        + sorted(COMMANDS_DIR.glob("*.md"))
        + [ROOT / "README.md", COPILOT_INSTRUCTIONS]
    )


def _tree(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


def test_three_public_skills_one_per_role():
    assert [p.name for p in SKILLS] == [
        "energyincloud-customer",
        "energyincloud-distributor",
        "energyincloud-installer",
    ]


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_frontmatter_keys_exactly_name_and_description(skill: Path):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    assert _frontmatter_keys(text) == {"name", "description"}
    assert f"name: {skill.name}\n" in text


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_skill_under_500_lines(skill: Path):
    assert len((skill / "SKILL.md").read_text(encoding="utf-8").splitlines()) < 500


def test_copilot_instructions_within_limit():
    # Declarative agent manifest 1.8: instructions are 8,000 characters or less.
    assert len(COPILOT_INSTRUCTIONS.read_text(encoding="utf-8")) <= 8000


@pytest.mark.parametrize("skill", SKILLS, ids=lambda p: p.name)
def test_local_links_resolve(skill: Path):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    md_links = re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text)
    code_paths = re.findall(r"`(references/[^`\s]+)`", text)
    targets = [t for t in md_links if not re.match(r"^[a-z]+:", t)] + code_paths
    assert code_paths, "SKILL.md is expected to reference its references/ files"
    missing = [t for t in targets if not (skill / t).is_file()]
    assert not missing, f"unresolved links: {missing}"


@pytest.mark.parametrize("path", _public_texts(), ids=lambda p: str(p.relative_to(ROOT)))
def test_no_vendor_tokens(path: Path):
    hits = VENDOR_RE.findall(path.read_text(encoding="utf-8"))
    assert not hits, f"vendor tokens in {path.name}: {hits}"


def test_skills_commands_and_copilot_match_the_generated_tree():
    if not GENERATED.is_dir():
        pytest.skip("triage-api checkout not present next to this repo")
    assert _tree(SKILLS_DIR) == _tree(GENERATED / "skills")
    assert _tree(COMMANDS_DIR) == _tree(GENERATED / "commands")
    assert COPILOT_INSTRUCTIONS.read_bytes() == (GENERATED / "copilot" / "instruction.txt").read_bytes()
