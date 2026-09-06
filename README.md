# AgentCannabis

AgentCannabis is a public Agent Skills repository for Canadian cannabis compliance, quality, operations governance, and evidence-review workflows. It packages a frozen Master Taxonomy v1.0 of 233 atomic skills into 251 installable skill folders, including 18 professional role skillsets.

AgentCannabis is designed for agents that can read local skill folders, project routing files, or GitHub Copilot Agent Skills. GitHub Copilot is a supported distribution path, not the whole product.

## Current release

- Release: `v1.0.3`
- Repository: `https://github.com/jeremylongworth-source/AgentCannabis`
- Status: `V1_READY`
- Atomic skills: 233
- Professional skillsets: 18
- Installable skill folders: 251
- Wiki: `https://github.com/jeremylongworth-source/AgentCannabis/wiki`

The roadmap is complete on `main`, the repository is public, the GitHub wiki is published, and all 18 professional skillsets are installable from the public release tag with `gh skill install`.

## What AgentCannabis does

AgentCannabis helps an AI agent produce bounded review artifacts such as:

- licence, role, site-area, product-authority, and activity-authority evidence reviews
- cannabis quality-system and GPP record checks
- lot, batch, inventory, CTLS-readiness, complaint, recall, and adverse-reaction evidence packages
- cultivation, post-harvest, processing, preventive-control, and quality-control record gap reviews
- source-currentness checks that separate access date, consolidation date, amendment date, effective date, and applicability
- responsible-human handoff briefs for regulated decisions

Every skill is structured to separate known facts, assumptions, missing evidence, source limits, risk routes, and next responsible reviewer actions.

## What AgentCannabis does not do

AgentCannabis provides review assistance only. It does not authorize cannabis production, legal compliance, QAP approval, lot release, CTLS or CRA filing, pesticide use, engineering operation, hazardous extraction, pressure tuning, bypass activity, record concealment, signatures, submissions, or professional sign-off.

Requests for regulated decisions or unsafe operational instructions are routed to bounded evidence review and qualified human review.

## Quick start

Clone the repository:

```powershell
git clone https://github.com/jeremylongworth-source/AgentCannabis.git
cd AgentCannabis
```

Run the repository validation gate:

```powershell
.\scripts\validate-all.ps1
```

Preview GitHub skill packaging:

```powershell
gh skill publish . --dry-run
```

Install a published professional skillset into a Git project for GitHub Copilot:

```powershell
gh skill install jeremylongworth-source/AgentCannabis skills/cannabis-compliance-specialist --agent github-copilot --scope project --pin v1.0.3
```

For non-Copilot local agent hosts, start with one of the root routing templates in `agents/`, then load the selected skill folder from `skills/`.

## First useful prompt

After installing or loading `cannabis-compliance-specialist`, test with fictional records:

```text
Use $cannabis-compliance-specialist to review this fictional licensed-site package for missing licence, role, inventory, quality, and source-currentness evidence. Do not approve or submit anything. Return a bounded evidence review with gaps and responsible-human next steps.
```

A good response should identify the selected member workflows, preserve missing evidence, avoid legal or QAP sign-off, and clearly state what must be reverified against current primary sources.

## Professional skillsets

| Skillset | Focus |
| --- | --- |
| `cannabis-compliance-specialist` | licence, role, product, inventory, reporting, complaints, safety, and audit evidence |
| `cannabis-operations-manager` | end-to-end operational governance, compliance evidence, quality systems, inventory, post-market, and safety escalation |
| `cannabis-processing-technician` | processing records, material intake, batch records, control measures, and deviation evidence |
| `cannabis-production-manager` | cross-stage production evidence, resource and deviation review, hazard escalation, records, and inventory impacts |
| `cannabis-quality-systems-specialist` | quality-system records, document control, training, CAPA, product quality, and post-market evidence |
| `controlled-environment-cultivation-specialist` | environmental monitoring evidence, trend review, sensor coverage, and qualified escalation |
| `ctls-inventory-specialist` | inventory reconciliation, CTLS readiness, loss/theft packages, destruction records, and discrepancy review |
| `cultivation-manager-support` | cultivation governance, capacity, deviations, people/role evidence, and safety escalation |
| `cultivation-technician` | daily cultivation record review, monitoring gaps, crop observations, and escalation packages |
| `drying-curing-specialist` | drying, curing, moisture, water activity, storage, and microbial-risk evidence review |
| `master-grower-support` | crop-cycle evidence, plant health, environment records, and production variance review without optimization instructions |
| `plant-health-specialist` | plant-health evidence, pest/disease observations, treatment records, and quality trend handoff |
| `post-harvest-manager` | post-harvest workflow control, holds, quality packages, inventory, deviations, and complaints |
| `post-harvest-technician` | harvest identity, intake, handling, drying, curing, and quality-record gaps |
| `preventive-controls-specialist` | hazard analysis, process controls, corrective actions, SOP execution, and safety escalation |
| `processing-manager-support` | processing authority, flow, yield reconciliation, hazard routing, GPP controls, and inventory review |
| `qap-support` | QAP responsibility evidence, quality systems, product records, complaints, recalls, holds, and adverse-reaction packages |
| `quality-control-specialist` | sampling, COA review, OOS evidence, specifications, product quality records, and release package support |

Each professional skillset is a self-contained skill under `skills/<skillset-name>/` with a matching manifest under `skillsets/<skillset-name>.json`, bundled member index, source snapshot, scenario specifications, and `agents/openai.yaml` metadata.

See [skillsets/README.md](skillsets/README.md) and the [Skillsets wiki page](wiki/Skillsets.md) for member counts and role-level routing.

## Portable agent routing

The root `agents/` directory follows the AgentSkills-style project routing convention:

- `agents/AGENTS.base.md`: base routing and safety boundaries
- `agents/AGENTS.full.md`: full AgentCannabis routing across all professional skillsets
- `agents/AGENTS.<skillset>.md`: focused routing for one professional role

These files let Codex-style and local-agent workflows use AgentCannabis without installing through GitHub Copilot.

## Repository structure

| Path | Purpose |
| --- | --- |
| `skills/` | 233 atomic skills and 18 professional skillset wrappers |
| `skillsets/` | Professional composition manifests and skillset README |
| `agents/` | AgentSkills-style routing templates |
| `catalog/` | Authored profile inputs used by builders |
| `sources/` | Machine-readable source registry snapshots |
| `docs/architecture/` | Taxonomy, scope, licence, role, activity, and hazard contracts |
| `docs/standards/` | Authoring, evidence, source, output, testing, and evaluation standards |
| `docs/development/` | Roadmap evidence, audit trail, evaluation reports, and peer consistency review |
| `docs/setup/` | Portable Agent Skills setup guidance |
| `docs/guides/` | Copilot installation and developer onboarding guides |
| `scripts/` | Import, build, install, metadata, routing-template, and validation tools |
| `tests/` | Deterministic review-gate tests |
| `wiki/` | Source pages for the GitHub wiki |

## Validation and evidence

Run the supported validation wrapper from the repository root:

```powershell
.\scripts\validate-all.ps1
```

The wrapper runs full structural validation, source metadata validation, and deterministic review-gate tests.

The release evidence also includes forward, integrated, adversarial, install, and peer consistency reports under `docs/development/`.

## Documentation

Start here:

- [Agent Skills setup](docs/setup/agent-skills.md)
- [Copilot installation guide](docs/guides/copilot-installation.md)
- [Developer onboarding](docs/guides/developer-onboarding.md)
- [Master taxonomy](docs/architecture/master-taxonomy-v1.md)
- [Acceptance criteria](docs/development/acceptance-criteria.md)
- [Final audit](docs/development/CC-39-final-audit.md)
- [GitHub wiki source](wiki/Home.md)

## Roadmap status

The roadmap is tracked in [ROADMAP.md](ROADMAP.md) and [docs/development/wave-status.json](docs/development/wave-status.json). A wave is treated as ready only when its evidence, limits, and next maintenance action are recorded.

`V1_READY` means the repository roadmap and distribution requirements are complete. It does not mean the skills provide legal advice, engineering approval, QAP approval, lot release, filing authorization, or site-specific compliance certification.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding or changing skills. Contributions must preserve the frozen 233-skill Master Taxonomy v1.0, self-contained skill packages, current-source limits, human approval boundaries, fictional test fixtures, structural validation, and review-gate coverage.

## Security and safety

Report security issues through [SECURITY.md](SECURITY.md). Do not include real commercial cannabis records, secrets, licence credentials, CTLS credentials, CRA credentials, signatures, or confidential regulated-site data in issues, tests, examples, or pull requests.

## License

MIT. See [LICENSE](LICENSE).
