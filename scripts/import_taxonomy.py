"""Import the supplied taxonomy without treating audit annotations as new skills."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [12, 10, 12, 12, 13, 12, 13, 12, 10, 13, 12, 12, 23, 16, 14, 16, 11, 10]
STAGES = ["federal-governance", "site-governance", "starting-material-records", "crop-planning-review",
          "environment-records", "root-zone-records", "plant-health-records", "crop-and-harvest-records",
          "post-harvest-intake", "post-harvest-quality", "processing-governance", "hazard-review",
          "quality-system", "testing-and-quality", "product-compliance", "traceability-and-reporting",
          "post-market", "workplace-and-improvement"]

def parse_taxonomy(text):
    families = []
    blocks = list(re.finditer(r"(?m)^# FAMILY (\d{2})\s*\n# ([^\r\n]+)", text))
    for pos, match in enumerate(blocks):
        end = blocks[pos + 1].start() if pos + 1 < len(blocks) else text.index("# Final count", match.end())
        body = text[match.end():end]
        body = body.split("Removed:")[0]
        names = []
        for block in re.findall(r"```text\s*\n(.*?)```", body, flags=re.S):
            for line in block.splitlines():
                line = line.strip()
                if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)+", line) and line not in names:
                    names.append(line)
        declared = int(re.search(r"\*\*Count: (\d+)\*\*", body).group(1))
        if len(names) != declared:
            raise ValueError(f"Family {match[1]} has {len(names)} imported names; expected {declared}")
        families.append({"id": match[1], "name": match[2], "count": declared, "skills": names})
    if [f["count"] for f in families] != COUNTS:
        raise ValueError("Family counts differ from the supplied v1 contract")
    names = [n for f in families for n in f["skills"]]
    if len(names) != 233 or len(set(names)) != 233:
        raise ValueError("Expected exactly 233 unique atomic names")
    return families

def metadata(family, name):
    number = int(family["id"])
    provincial = number == 18 or name == "identify-engineering-escalation"
    hazard = "ENGINEERING_BOUNDARY" if name == "identify-engineering-escalation" else (
        "HAZARDOUS_PROCESS" if number == 12 or name == "review-co2-management-context" else
        "CONTROLLED_PROCESS" if number in (7, 9, 10, 11, 13, 14, 15, 17, 18) else "ROUTINE_PROCESS")
    regulated = number in (1, 2, 7, 12, 13, 14, 15, 16, 17, 18)
    role = ("Qualified discipline professional and authorized site reviewer" if provincial else
            "QAP responsibility / authorized quality reviewer" if number in (12, 13, 14, 15, 17) else
            "Responsible Person / authorized regulatory reviewer" if number in (1, 2, 16) else
            "Master Grower responsibility / authorized records reviewer" if number in range(3, 9) else
            "Authorized operations and quality reviewer")
    return {
        "family": family["id"], "tier": "SPECIALIST" if provincial else "ADVANCED" if number == 12 else "CORE",
        "production_stage": STAGES[number - 1],
        "jurisdiction": "PROVINCIAL_REQUIRED" if provincial else "CANADA_FEDERAL",
        "licence_dependency": "Verify actual licence class, authorized activity, site/area and conditions; general research may describe unknowns",
        "responsible_role": role,
        "regulatory_sensitivity": "HIGHLY_REGULATED" if regulated else "REGULATED",
        "hazard_class": hazard,
        "human_approval_required": "true" if regulated or hazard != "ROUTINE_PROCESS" else "false-for-review-only; required-before-implementation",
        "source_freshness": "HIGH: reverify at decision time; repository review interval 30 days; access date is not legal currency",
    }

def main():
    original = (ROOT / "docs/development/taxonomy-source.md").read_text(encoding="utf-8-sig")
    families = parse_taxonomy(original)
    records = [{"name": n, **metadata(f, n)} for f in families for n in f["skills"]]
    index = {"schema_version": "1.0", "taxonomy_version": "1.0", "atomic_count": 233,
             "family_count": 18, "source": "docs/development/taxonomy-source.md",
             "aliases": {"identify-responsible-role": ["identify-required-site-roles", "map-site-role-responsibilities"]},
             "families": families, "skills": records}
    path = ROOT / "docs/architecture/taxonomy-index.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    preface = ("# Supplied taxonomy authority\n\nThis preserves the user's supplied v1 taxonomy. Its historical audit verdicts describe the taxonomy, not completed repository implementation. "
               "The current user's full-project request and ROADMAP.md govern execution; CC-10 remains the architecture gate before mass authoring. "
               "The machine-readable canonical index is [taxonomy-index.yaml](taxonomy-index.yaml), encoded as JSON-compatible YAML. "
               "The diagram alias is documented in [site-role-routing.md](site-role-routing.md).\n\n---\n\n")
    (ROOT / "docs/architecture/master-taxonomy-v1.md").write_text(preface + original, encoding="utf-8")
    print(json.dumps({"atomic_skills": len(records), "families": len(families), "counts": COUNTS}))

if __name__ == "__main__":
    main()
