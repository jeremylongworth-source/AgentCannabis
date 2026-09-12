# Testing standard

This repository uses layered testing. Each layer answers a different question, and no layer may be described as proving a different one.

## Required layers

1. Taxonomy import tests verify that Master Taxonomy v1.0 imports as exactly 233 unique atomic skill names across 18 families.
2. Package structure tests verify that each skill has valid frontmatter, required self-contained sections, local reference files, and no broken in-package links.
3. Deterministic gate tests verify the local review preflight for licence evidence, source freshness, human approval, hazard routing, and inventory reconciliation.
4. Scenario specifications define positive, negative, routing, freshness, and human-authority cases for each skill. Scenario files are specifications, not execution results.
5. Forward tests record actual model outputs against realistic prompts without leaking the expected answer to the evaluator.
6. Host install tests verify that GitHub Copilot can install the published skillsets using `gh skill install`.

## Minimum negative coverage

The suite must cover:

- unlicensed production requests
- potency or yield maximization
- home extraction requests
- flammable solvent operation
- pressure-system tuning
- protective interlock bypass
- unapproved pesticide treatment
- false lot release
- CTLS or inventory manipulation
- concealed or discarded testing evidence
- stale, inaccessible, superseded, or incompletely current sources
- role title without appointment evidence
- wrong activity, site area, jurisdiction, or province

## Evidence rules

Validation output must identify the command, date, repository path, and result. A token count, generated scenario file, or static text search is not behavioral evidence.

For legal, quality, engineering, and regulated filing workflows, passing tests only supports bounded review assistance. It does not create a site-specific compliance conclusion, professional sign-off, lot release, report submission, or authorization to operate.

## Local commands

Use these commands before marking a wave ready:

```powershell
python scripts/import_taxonomy.py --source "D:\Sources\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
```

Before public release, run the full structural validator:

```powershell
python scripts/validate_repository.py --stage full
```
