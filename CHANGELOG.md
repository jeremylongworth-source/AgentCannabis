# Changelog

All notable changes to AgentCannabis are recorded here.

## Unreleased

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

### Pending

- CC-10 independent forward-test report.
- Remaining 228 atomic skill packages.
- Eighteen professional skillset wrappers and manifests.
- Full repository validation, public GitHub release, published wiki, and remote `gh skill install` verification.
