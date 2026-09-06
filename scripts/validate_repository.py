"""Structural validator for the AgentCannabis skill repository.

This validator checks package structure and repository invariants. It does not
prove skill behavior, legal correctness, or GitHub host installability.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_METADATA = {
    "family",
    "tier",
    "production_stage",
    "jurisdiction",
    "licence_dependency",
    "responsible_role",
    "regulatory_sensitivity",
    "hazard_class",
    "human_approval_required",
    "source_freshness",
    "package_kind",
}

REQUIRED_SECTIONS = {
    "## Triggers",
    "## Non-triggers",
    "## Inputs",
    "## Assumptions and dependencies",
    "## Licence requirements and responsible role",
    "## Procedure",
    "## Evidence and source requirements",
    "## Hazard behavior and human approval",
    "## Outputs and limitations",
    "## Tests",
}

SCENARIO_CASES = {"positive", "negative", "routing", "freshness", "human-authority"}
REFERENCE_NAMES = {
    "build-crop-monitoring-plan",
    "determine-authorized-cannabis-activity",
    "assess-lot-release-readiness",
    "classify-processing-hazard",
    "identify-engineering-escalation",
}
PROFESSIONAL_SKILLSETS = {
    "cultivation-technician",
    "cultivation-manager-support",
    "master-grower-support",
    "plant-health-specialist",
    "controlled-environment-cultivation-specialist",
    "post-harvest-technician",
    "drying-curing-specialist",
    "post-harvest-manager",
    "cannabis-processing-technician",
    "processing-manager-support",
    "preventive-controls-specialist",
    "quality-control-specialist",
    "qap-support",
    "cannabis-quality-systems-specialist",
    "cannabis-compliance-specialist",
    "ctls-inventory-specialist",
    "cannabis-production-manager",
    "cannabis-operations-manager",
}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} has unterminated frontmatter")
    raw = text[4:end].splitlines()
    body = text[end + 5 :]
    data: dict[str, object] = {}
    current_map: dict[str, str] | None = None
    for line in raw:
        if not line.strip():
            continue
        if line.startswith("  "):
            if current_map is None:
                fail(f"{path.relative_to(ROOT)} has nested frontmatter without a parent")
            key, value = parse_key_value(line.strip(), path)
            current_map[key] = value
            continue
        key, value = parse_key_value(line, path)
        if value == "":
            current_map = {}
            data[key] = current_map
        else:
            current_map = None
            data[key] = value
    return data, body


def parse_key_value(line: str, path: Path) -> tuple[str, str]:
    if ":" not in line:
        fail(f"{path.relative_to(ROOT)} has invalid frontmatter line: {line}")
    key, value = line.split(":", 1)
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            fail(f"{path.relative_to(ROOT)} has invalid quoted value for {key}")
    return key.strip(), str(value)


def validate_taxonomy() -> list[dict[str, object]]:
    data = load_json(ROOT / "docs/architecture/taxonomy-index.yaml")
    if data.get("atomic_count") != 233:
        fail("Taxonomy atomic_count must be 233")
    if data.get("family_count") != 18:
        fail("Taxonomy family_count must be 18")
    skills = data.get("skills")
    if not isinstance(skills, list) or len(skills) != 233:
        fail("Taxonomy must contain exactly 233 skill records")
    names = [record.get("name") for record in skills if isinstance(record, dict)]
    if len(names) != len(set(names)):
        fail("Taxonomy contains duplicate skill names")
    family_counts: dict[str, int] = {}
    for record in skills:
        if not isinstance(record, dict):
            fail("Taxonomy skill record is not an object")
        for key in REQUIRED_METADATA - {"package_kind"}:
            if key not in record:
                fail(f"Taxonomy record {record.get('name')} missing {key}")
        family = str(record.get("family"))
        family_counts[family] = family_counts.get(family, 0) + 1
    families = data.get("families")
    if not isinstance(families, list):
        fail("Taxonomy families must be a list")
    expected = {str(f["id"]).zfill(2): int(f["count"]) for f in families}
    if family_counts != expected:
        fail(f"Family counts mismatch: expected {expected}, got {family_counts}")
    return skills


def validate_sources() -> None:
    source_files = sorted((ROOT / "sources").glob("*.json"))
    if not source_files:
        fail("No source registry files found")
    ids: set[str] = set()
    required = {"id", "source_title", "organization", "jurisdiction", "source_url", "last_verified", "targeted_claim", "limitations"}
    for source_file in source_files:
        data = load_json(source_file)
        sources = data.get("sources")
        if not isinstance(sources, list) or not sources:
            fail(f"{source_file.relative_to(ROOT)} must contain source records")
        for source in sources:
            if not isinstance(source, dict):
                fail(f"{source_file.relative_to(ROOT)} contains non-object source")
            missing = required - set(source)
            if missing:
                fail(f"Source {source.get('id')} missing fields: {sorted(missing)}")
            if source["id"] in ids:
                fail(f"Duplicate source id: {source['id']}")
            ids.add(str(source["id"]))
            if not str(source["source_url"]).startswith("https://"):
                fail(f"Source {source['id']} must use an https URL")


def validate_links(path: Path, body: str) -> None:
    for match in re.finditer(r"\]\(([^)]+)\)", body):
        target = match.group(1)
        if "://" in target or target.startswith("#"):
            continue
        link_path = (path.parent / target).resolve()
        try:
            link_path.relative_to(path.parent.resolve())
        except ValueError:
            fail(f"{path.relative_to(ROOT)} links outside its package: {target}")
        if not link_path.exists():
            fail(f"{path.relative_to(ROOT)} has broken local link: {target}")


def validate_skill(name: str, *, expected_kind: str = "atomic") -> None:
    path = ROOT / "skills" / name / "SKILL.md"
    if not path.is_file():
        fail(f"Missing skill: {name}")
    frontmatter, body = parse_frontmatter(path)
    if frontmatter.get("name") != name:
        fail(f"{name} frontmatter name mismatch")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        fail(f"{name} missing description")
    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        fail(f"{name} missing metadata map")
    missing = REQUIRED_METADATA - set(metadata)
    if missing:
        fail(f"{name} missing metadata fields: {sorted(missing)}")
    if metadata.get("package_kind") != expected_kind:
        fail(f"{name} package_kind must be {expected_kind}")
    for key, value in metadata.items():
        if not isinstance(value, str) or value == "":
            fail(f"{name} metadata {key} must be a non-empty string")
    missing_sections = [section for section in sorted(REQUIRED_SECTIONS) if section not in body]
    if missing_sections:
        fail(f"{name} missing sections: {missing_sections}")
    validate_links(path, body)
    refs = path.parent / "references"
    if not (refs / "review-contract.md").is_file():
        fail(f"{name} missing review contract")
    if not (refs / "sources.json").is_file():
        fail(f"{name} missing source snapshot")
    scenarios = load_json(refs / "scenarios.json")
    cases = scenarios.get("cases")
    if not isinstance(cases, list):
        fail(f"{name} scenarios must contain cases")
    case_ids = {case.get("id") for case in cases if isinstance(case, dict)}
    if case_ids != SCENARIO_CASES:
        fail(f"{name} scenario ids mismatch: {case_ids}")


def validate_reference_stage() -> None:
    validate_taxonomy()
    validate_sources()
    for name in sorted(REFERENCE_NAMES):
        validate_skill(name)


def validate_full_stage() -> None:
    taxonomy_records = validate_taxonomy()
    validate_sources()
    for record in taxonomy_records:
        validate_skill(str(record["name"]))
    manifests = ROOT / "skillsets"
    if not manifests.is_dir():
        fail("Missing skillsets directory")
    for name in sorted(PROFESSIONAL_SKILLSETS):
        manifest = load_json(manifests / f"{name}.json")
        if manifest.get("name") != name:
            fail(f"Skillset {name} manifest name mismatch")
        members = manifest.get("included_skills")
        if not isinstance(members, list) or not members:
            fail(f"Skillset {name} must include skills")
        if len(members) != len(set(members)):
            fail(f"Skillset {name} contains duplicate members")
        validate_skill(name, expected_kind="professional-skillset")
        for member in members:
            if not (ROOT / "skills" / str(member) / "SKILL.md").is_file():
                fail(f"Skillset {name} references missing member {member}")
    skill_folders = [p.name for p in (ROOT / "skills").iterdir() if p.is_dir()]
    if len(skill_folders) != 251:
        fail(f"Expected 251 skill folders, found {len(skill_folders)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["reference", "full"], required=True)
    args = parser.parse_args()
    try:
        if args.stage == "reference":
            validate_reference_stage()
        else:
            validate_full_stage()
    except ValidationError as exc:
        print(json.dumps({"status": "FAIL", "stage": args.stage, "error": str(exc)}, indent=2))
        raise SystemExit(1)
    print(json.dumps({"status": "PASS", "stage": args.stage, "scope": "structural-only"}, indent=2))


if __name__ == "__main__":
    main()
