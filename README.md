# AgentCannabis

Portable Agent Skills for bounded Canadian cannabis compliance, quality,
operations-governance, and evidence-review workflows.

[GitHub repository](https://github.com/jeremylongworth-source/AgentCannabis) ·
[current public tag](https://github.com/jeremylongworth-source/AgentCannabis/tree/v1.0.5) ·
[GitHub wiki](https://github.com/jeremylongworth-source/AgentCannabis/wiki) ·
[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

AgentCannabis gives an AI agent structured ways to review records, identify
missing evidence, preserve source limits, and prepare a handoff for the
responsible human or qualified professional. It is a portable Agent Skills
repository. GitHub Copilot is one supported distribution path; the same
packages can be loaded by local agent hosts that understand skill folders or
project routing files.

## Release status

| Item | Current state |
| --- | --- |
| Current public tag | [`v1.0.5`](https://github.com/jeremylongworth-source/AgentCannabis/tree/v1.0.5) |
| Readiness | `V1_READY` for repository and public distribution requirements |
| Atomic skills | 233 across 18 frozen taxonomy families |
| Professional skillsets | 18 self-contained role packages |
| Installable skill folders | 251 (233 atomic skills plus 18 wrappers) |
| Public distribution | GitHub repository, wiki, and release-tag installs verified |

The readiness decision is documented in [the final audit](docs/development/CC-39-final-audit.md).
`V1_READY` describes repository, validation, documentation, and distribution
evidence. It does not grant legal, regulatory, QAP, engineering, tax, filing,
lot-release, or site-operating authority.

## Who this is for

- Canadian licensed producers and cannabis teams that need review-ready
  evidence packages.
- Quality, compliance, cultivation, post-harvest, processing, inventory, and
  operations professionals who need structured handoffs.
- AI-agent builders who want portable, source-aware skills with explicit
  approval and safety boundaries.
- Maintainers and evaluators who need deterministic validation, scenarios, and
  release evidence around an Agent Skills repository.

## What it covers

The repository supports bounded review work such as:

- licence, role, site-area, product-authority, and activity-authority evidence
  reviews;
- GPP, quality-system, training, CAPA, sanitation, and document-control
  record checks;
- cultivation, post-harvest, drying, curing, processing, preventive-control,
  and quality-control evidence reviews;
- lot, batch, inventory, CTLS-readiness, complaint, recall, and
  adverse-reaction evidence packages;
- source-currentness checks that distinguish access, consolidation,
  amendment, effective, and applicability dates; and
- responsible-human handoff briefs that state known facts, missing evidence,
  uncertainty, and the next review owner.

## Boundaries

AgentCannabis provides review assistance. It does not authorize or perform
cannabis production, legal compliance, QAP approval, lot release, CTLS or CRA
filing, pesticide use, engineering operation, hazardous extraction, pressure
tuning, bypass activity, record concealment, signatures, submissions, or
professional sign-off.

When a request crosses a boundary, the skills redirect to a bounded evidence
review with source limits, risk routing, and qualified-human next steps. Read
[Safety Boundaries](wiki/Safety-Boundaries.md) and
[Prohibited Capabilities](docs/architecture/prohibited-capabilities.md) before
using the packages for regulated work.

## Quick start

### Install a professional skillset

Requirements are Git, a destination Git project, and GitHub CLI with
`gh skill` support. Run the install from the destination project:

```powershell
gh skill preview jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist@v1.0.5
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.5
```

The example targets GitHub Copilot. `gh skill install` also supports other
Agent Skills hosts; choose the host documented by your installed GitHub CLI.
Use a release tag for reproducible installs and `main` only when you want the
moving development branch. See the [installation guide](docs/guides/copilot-installation.md)
for atomic skills, user scope, pinning, verification, and troubleshooting.

### Load the portable packages locally

For a local agent host that reads project instructions:

1. Start with `agents/AGENTS.base.md`, `agents/AGENTS.full.md`, or the focused
   `agents/AGENTS.<skillset-name>.md` template.
2. Load the selected `skills/<name>/SKILL.md`.
3. Load its references only when the task requires them.
4. Preserve source-currentness limits and human-approval boundaries.

See [Agent Skills setup](docs/setup/agent-skills.md) and
[Agent Routing](wiki/Agent-Routing.md) for the portable path.

### Try a first review

Use fictional records after installation or local loading:

```text
Use $cannabis-compliance-specialist to review this fictional licensed-site
package for missing licence, role, inventory, quality, and source-currentness
evidence. Do not approve, sign, submit, release, or operate anything. Return a
bounded evidence review with gaps and responsible-human next steps.
```

A useful result identifies the selected workflows, preserves missing evidence,
states source limits, and separates review assistance from decisions reserved
for an authorized human or qualified professional.

## Professional skillsets

Professional packages are role-level wrappers around the 233 atomic skills.
Each wrapper is self-contained under `skills/<skillset-name>/`, with a matching
manifest in `skillsets/`, bundled references, scenarios, and `agents/openai.yaml`
metadata.

| Skillset | Primary focus |
| --- | --- |
| `cannabis-compliance-specialist` | licence, role, product, inventory, reporting, complaints, safety, and audit evidence |
| `cannabis-operations-manager` | end-to-end operational governance, quality systems, inventory, post-market, and safety escalation |
| `cannabis-processing-technician` | processing records, material intake, batch records, controls, and deviations |
| `cannabis-production-manager` | cross-stage production evidence, resource and deviation review, and inventory impacts |
| `cannabis-quality-systems-specialist` | quality systems, document control, training, CAPA, product quality, and post-market evidence |
| `controlled-environment-cultivation-specialist` | environmental monitoring, trend review, sensor coverage, and escalation |
| `ctls-inventory-specialist` | inventory reconciliation, CTLS readiness, loss/theft, destruction, and discrepancy review |
| `cultivation-manager-support` | cultivation governance, capacity, deviations, role evidence, and safety escalation |
| `cultivation-technician` | daily cultivation record review, monitoring gaps, and escalation packages |
| `drying-curing-specialist` | drying, curing, moisture, water activity, storage, and microbial-risk evidence |
| `master-grower-support` | crop-cycle evidence, plant health, environment records, and production variance review |
| `plant-health-specialist` | plant-health evidence, pest/disease observations, treatment records, and quality handoff |
| `post-harvest-manager` | post-harvest control, holds, quality packages, inventory, deviations, and complaints |
| `post-harvest-technician` | harvest identity, intake, handling, drying, curing, and quality-record gaps |
| `preventive-controls-specialist` | hazard analysis, process controls, corrective actions, and safety escalation |
| `processing-manager-support` | processing authority, flow, yield reconciliation, hazard routing, GPP controls, and inventory review |
| `qap-support` | QAP responsibility evidence, quality systems, product records, complaints, recalls, holds, and adverse-reaction packages |
| `quality-control-specialist` | sampling, COA review, OOS evidence, specifications, and release-package support |

See [skillsets/README.md](skillsets/README.md) for the complete composition
index and [the Skillsets wiki page](wiki/Skillsets.md) for routing guidance.

## How the repository is organized

| Path | Purpose |
| --- | --- |
| `skills/` | 233 atomic skills and 18 professional wrappers |
| `skillsets/` | Professional composition manifests and package index |
| `agents/` | AgentSkills-style base, full, and focused routing templates |
| `catalog/` | Curated profile inputs used by generators |
| `sources/` | Machine-readable source registry snapshots |
| `docs/architecture/` | Taxonomy, scope, licence, role, activity, and hazard contracts |
| `docs/standards/` | Authoring, evidence, source, output, testing, and evaluation standards |
| `docs/development/` | Wave status, audit evidence, evaluations, and peer review |
| `docs/setup/` and `docs/guides/` | Portable setup, Copilot installation, and maintainer guidance |
| `scripts/` | Build, metadata, routing, install, publish, and validation tools |
| `tests/` | Deterministic review-gate tests and fictional fixtures |
| `wiki/` | Version-controlled source pages for the GitHub wiki |

## Validation and evidence

From a local clone, run the complete validation gate:

```powershell
.\scripts\validate-all.ps1
```

The gate runs structural validation, source-link validation, and deterministic
review-gate tests. Before publishing a skill repository, preview packaging
with the repository wrapper:

```powershell
.\scripts\publish_skill_repository.ps1 -DryRun
```

The wrapper applies Git's `safe.directory` setting only to the publish process
when needed on Windows-owned checkouts. It does not change global Git config.

Evaluation reports under `docs/development/evaluations/` distinguish scenario
specifications, captured forward tests, integrated workflows, adversarial
checks, and public install evidence. Passing installation proves packaging
availability; it does not prove legal correctness or future model behavior.

## Documentation map

- [GitHub wiki](https://github.com/jeremylongworth-source/AgentCannabis/wiki) — guided orientation for users and maintainers.
- [Wiki source](wiki/Home.md) — version-controlled wiki pages.
- [Master Taxonomy v1.0](docs/architecture/master-taxonomy-v1.md) — the frozen 233-skill authority.
- [Acceptance criteria](docs/development/acceptance-criteria.md) — release requirements and evidence.
- [Final audit](docs/development/CC-39-final-audit.md) — current readiness decision and limitations.
- [Roadmap](ROADMAP.md) — development authority and wave contracts.
- [Developer onboarding](docs/guides/developer-onboarding.md) — generator and validation workflow.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing skills, generators,
source records, or public documentation. Contributions must preserve the
frozen taxonomy, self-contained packages, current-source limits, human-
authority boundaries, fictional fixtures, and validation coverage.

Use [SECURITY.md](SECURITY.md) for security or safety-sensitive reports. Do
not publish secrets, credentials, signatures, live regulated-site records, or
confidential commercial data in issues, tests, examples, or pull requests.

## License

AgentCannabis is licensed under the [MIT License](LICENSE).
