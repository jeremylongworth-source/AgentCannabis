# AgentCannabis

AgentCannabis is an AI Agent Skills repository for Canadian cannabis compliance, quality, operations, and evidence-review workflows. It is built from a frozen Master Taxonomy v1.0 of 233 atomic skills across 18 families, then composed into professional skillsets for reusable agent workflows and GitHub Copilot installation.

The repository supports review assistance only. It does not authorize cannabis production, lot release, CTLS or CRA filing, pesticide use, engineering operation, hazardous extraction, or legal compliance decisions. Regulated decisions remain with the responsible authorized human or qualified professional.

## Current status

AgentCannabis v1.0 is ready. The roadmap is complete on `main`, the GitHub repository is public, the GitHub wiki is published, and all 18 professional skillsets install from both public `main` and the public `v1.0.1` tag with `gh skill install`.

## Quick local checks

```powershell
python scripts/import_taxonomy.py --source "C:\Users\jerem\Desktop\Taxonomy Canadian Cannabis Skill Repositor.txt" --output docs/architecture/taxonomy-index.yaml
python -m unittest discover -s tests -v
python scripts/validate_repository.py --stage reference
gh skill publish D:\AgentCannabis --dry-run
```

## Use The Skills

```powershell
gh skill install D:\AgentCannabis build-crop-monitoring-plan --from-local --dir D:\AgentCannabis\.verification\copilot-install
```

For any Agent Skills host, start with the relevant `skills/<name>/SKILL.md` and load referenced files only when needed. See `docs/setup/agent-skills.md` for portable usage guidance. Each skill includes `agents/openai.yaml` metadata for hosts that read it. GitHub Copilot users can install published professional skillsets from the public repository:

```powershell
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.1
```

## Repository map

- `skills/` contains portable Agent Skills packages with `SKILL.md`, `agents/openai.yaml`, and self-contained references.
- `skillsets/` contains professional composition manifests.
- `catalog/` contains authored skill profiles used by the builder.
- `docs/architecture/` contains taxonomy, scope, licence, role, activity, and hazard contracts.
- `docs/standards/` contains authoring, evidence, source, testing, and evaluation standards.
- `docs/research/` contains regulatory source registers and limitations.
- `scripts/` contains taxonomy import, skill building, review gate, validation, and installation helpers.
- `tests/` contains deterministic review-gate tests.
- `wiki/` contains source pages for the GitHub wiki.

## Validation

Run the peer-style validation wrapper from the repository root:

```powershell
.\scripts\validate-all.ps1
```

For GitHub skill packaging, also run:

```powershell
gh skill publish D:\AgentCannabis --dry-run
```

## Roadmap

The roadmap is tracked in `ROADMAP.md` and `docs/development/wave-status.json`. A wave is ready only when its evidence is present and its limits are recorded.

## Contributing

Read `CONTRIBUTING.md` before adding or changing skills. New skills must preserve the repository safety boundaries and pass the structural validator.

## License

MIT. See `LICENSE`.







