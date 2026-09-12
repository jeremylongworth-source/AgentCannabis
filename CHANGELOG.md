# Changelog

All notable changes to AgentCannabis are recorded here.

## Unreleased

### Changed

- Reworked the README around audience, package model, portable installation,
  first-use guidance, boundaries, validation, and evidence links.
- Expanded the wiki with professional installation, architecture, routing,
  evaluation, maintenance, contribution, and troubleshooting guidance.
- Corrected public documentation commands to use the scoped publish wrapper and
  removed local-machine paths from maintainer-facing setup examples.

### Validation

- `python .verification/check_public_docs.py` passes.
- `.\scripts\validate-all.ps1` passes.
- `.\scripts\publish_skill_repository.ps1 -DryRun` completes with only the
  GitHub tag-protection advisory.

## v1.0.4 - 2026-09-06

### Changed

- Added `scripts/publish_skill_repository.ps1` to run `gh skill publish` with a command-scoped Git `safe.directory` override on Windows-owned Codex checkouts.
- Updated README and wiki publishing validation commands to use the scoped wrapper instead of requiring a persistent global Git trust entry.

### Validation

- `.\scripts\validate-all.ps1` passes.
- `.\scripts\publish_skill_repository.ps1 -DryRun` completes without the false `not a git repository` warning.
- All 18 professional skillsets install from the public `v1.0.4` tag with `gh skill install`.

## v1.0.3 - 2026-09-06

### Changed

- Rewrote the public README for a professional open-source Agent Skills release.
- Expanded the GitHub wiki source into a complete user, maintainer, routing, taxonomy, source, evaluation, and FAQ guide.
- Updated release audit documentation to reflect the expanded public documentation surface.

### Validation

- `.\scripts\validate-all.ps1` passes.
- `.\scripts\publish_skill_repository.ps1 -DryRun` completes.
- All 18 professional skillsets install from the public `v1.0.3` tag with `gh skill install`.

## v1.0.2 - 2026-09-06

### Changed

- Added AgentSkills-style root routing templates under `agents/` for base, full, and all 18 professional skillsets.
- Added deterministic routing-template generation and validation.
- Corrected the peer consistency review to compare against `D:\CodexProject\AgentSkills` directly.

### Validation

- `.\scripts\validate-all.ps1` passes.
- `.\scripts\publish_skill_repository.ps1 -DryRun` completes.
- All 18 professional skillsets install from the public `v1.0.2` tag with `gh skill install`.

## v1.0.1 - 2026-09-06

### Changed

- Reframed AgentCannabis as a portable AI Agent Skills repository, with GitHub Copilot documented as one supported distribution path.
- Added `agents/openai.yaml` host metadata to all 251 installable skill folders.
- Added peer-style validation, GitHub workflow, source metadata audit, pull request template, issue templates, `.gitattributes`, setup docs, and skillset README coverage.

### Validation

- `.\scripts\validate-all.ps1` passes.
- `.\scripts\publish_skill_repository.ps1 -DryRun` passes with only the tag-protection advisory.
## v1.0.0 - 2026-09-05

### Added

- Imported Master Taxonomy v1.0 as a 233-skill, 18-family canonical index.
- Added architecture contracts for scope, prohibited capabilities, licence routing, site roles, activity authority, process hazards, engineering boundaries, and hazardous-process routing.
- Added standards for skill authoring, naming, output contracts, research evidence, regulatory sources, source freshness, GPP quality systems, testing, and evaluation.
- Added five CC-10 reference skill packages with self-contained references and scenario specifications.
- Added deterministic review-gate tests for licence evidence, source freshness, role evidence, human approval, hazard routing, and inventory reconciliation.
- Added structural repository validator and Copilot installation helper.
- Added federal and extension source registers with currentness limitations.


### Validation

- Reference structural validation passes with `python scripts/validate_repository.py --stage reference`.
- Review-gate unit tests pass with `python -m unittest discover -s tests -v`.
- GitHub skill publish dry-run passes for the reference-stage repository.
- Local `gh skill install --from-local` succeeds for the five reference skills.





