# Developer onboarding

AgentCannabis is a skill repository, not an application server. The first useful local task is to validate the taxonomy, deterministic gate, and reference skill packages.

## Prerequisites

- Windows with PowerShell
- Python 3.11 or newer
- Git
- GitHub CLI with `gh skill`

## First run

```powershell
python scripts/import_taxonomy.py --source "C:\Users\jerem\Desktop\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
gh skill publish D:\AgentCannabis --dry-run
```

## Common workflows

Regenerate reference skills:

```powershell
python scripts/build_skills.py --stage reference
```

Run full validation after all packages exist:

```powershell
python scripts/validate_repository.py --stage full
```

Install a skill locally for inspection:

```powershell
gh skill install D:\AgentCannabis build-crop-monitoring-plan --from-local --dir D:\AgentCannabis\.verification\copilot-install
```

## Key files

- `docs/architecture/taxonomy-index.yaml` is JSON-compatible YAML and is the canonical machine index.
- `catalog/reference-profiles.json` defines the five reference skills.
- `catalog/task-profiles.json` will define the remaining atomic skill profiles.
- `scripts/build_skills.py` generates skill packages from curated profiles.
- `scripts/validate_repository.py` verifies repository structure.
- `tests/test_review_gate.py` verifies deterministic review preflight behavior.

## Troubleshooting

If GitHub CLI cannot see the repository under elevated execution, pass a process-scoped safe directory:

```powershell
$env:GIT_CONFIG_COUNT='1'
$env:GIT_CONFIG_KEY_0='safe.directory'
$env:GIT_CONFIG_VALUE_0='D:/AgentCannabis'
```

If a legal source was accessed successfully, still verify its currentness before a site-specific conclusion. Access date is not the same as law currentness.
