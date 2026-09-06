"""Generate agents/openai.yaml metadata for every AgentCannabis skill package."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"missing frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise SystemExit(f"unterminated frontmatter: {path}")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith("  "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = json.loads(value)
        data[key] = str(value)
    return data


def display_name(name: str) -> str:
    acronyms = {"qap": "QAP", "ctls": "CTLS", "gpp": "GPP", "sop": "SOP", "thc": "THC", "whmis": "WHMIS", "co2": "CO2", "capa": "CAPA"}
    words = []
    for part in name.split("-"):
        words.append(acronyms.get(part, part.capitalize()))
    return " ".join(words)


def short_description(name: str, description: str) -> str:
    if description:
        first = description.split(".", 1)[0].strip()
    else:
        first = f"Review {name.replace('-', ' ')}"
    first = first.replace("AgentCannabis ", "")
    if len(first) > 120:
        first = first[:117].rstrip() + "..."
    return first


def quote(value: str) -> str:
    return json.dumps(value)


def main() -> None:
    count = 0
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            continue
        metadata = parse_frontmatter(skill_md)
        name = metadata["name"]
        description = metadata.get("description", "")
        agents_dir = skill_dir / "agents"
        agents_dir.mkdir(exist_ok=True)
        text = "interface:\n"
        text += f"  display_name: {quote(display_name(name))}\n"
        text += f"  short_description: {quote(short_description(name, description))}\n"
        text += f"  default_prompt: {quote(f'Use ${name} to prepare a bounded AgentCannabis review with evidence gaps, source-currentness limits, and responsible human decisions clearly separated.')}\n"
        (agents_dir / "openai.yaml").write_text(text, encoding="utf-8")
        count += 1
    print(json.dumps({"status": "PASS", "generated": count}))


if __name__ == "__main__":
    main()
