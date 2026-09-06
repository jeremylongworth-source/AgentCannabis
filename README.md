# AgentCannabis

AgentCannabis is a GitHub Copilot skill repository for Canadian cannabis compliance, quality, operations, and evidence-review workflows. It is built from a frozen Master Taxonomy v1.0 of 233 atomic skills across 18 families, then composed into professional skillsets for Copilot installation.

The repository supports review assistance only. It does not authorize cannabis production, lot release, CTLS or CRA filing, pesticide use, engineering operation, hazardous extraction, or legal compliance decisions. Regulated decisions remain with the responsible authorized human or qualified professional.

## Current status

Reference-stage packaging is implemented for the five CC-10 skills. The full v1.0 release requires the CC-10 forward-test report, the remaining atomic skill profiles, the 18 professional wrappers, full structural validation, public GitHub publication, wiki publication, and remote `gh skill install` verification.

## Quick local checks

```powershell
python scripts/import_taxonomy.py --source "C:\Users\jerem\Desktop\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
gh skill publish D:\AgentCannabis --dry-run
```

## Install a local reference skill

```powershell
gh skill install D:\AgentCannabis build-crop-monitoring-plan --from-local --dir D:\AgentCannabis\.verification\copilot-install
```

Published professional skillsets will use this shape after v1.0 is tagged:

```powershell
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.0
```

## Repository map

- `skills/` contains Copilot skill packages.
- `skillsets/` will contain professional composition manifests.
- `catalog/` contains authored skill profiles used by the builder.
- `docs/architecture/` contains taxonomy, scope, licence, role, activity, and hazard contracts.
- `docs/standards/` contains authoring, evidence, source, testing, and evaluation standards.
- `docs/research/` contains regulatory source registers and limitations.
- `scripts/` contains taxonomy import, skill building, review gate, validation, and installation helpers.
- `tests/` contains deterministic review-gate tests.
- `wiki/` contains source pages for the GitHub wiki.

## Roadmap

The roadmap is tracked in `ROADMAP.md` and `docs/development/wave-status.json`. A wave is ready only when its evidence is present and its limits are recorded.

## Contributing

Read `CONTRIBUTING.md` before adding or changing skills. New skills must preserve the repository safety boundaries and pass the structural validator.

## License

MIT. See `LICENSE`.
